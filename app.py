import gradio as gr
import numpy as np
import pickle

# Load the model
with open("final_model.sav", "rb") as f:
    model = pickle.load(f)

# Load encoder model
with open("subcounty_encoder.pkl", 'rb') as f:
    encoder = pickle.load(f)

# Define the subcounty mapping
subcounty_mapping = dict(zip(encoder.categories_[0], range(len(encoder.categories_[0]))))

def predict(*args):
    # Convert subcounty to numerical value
    if args[0] is None or args[3] is None or args[4] is None:
        return gr.Error('Please fill in missing field')
    else:
        sub_county_num = subcounty_mapping[args[0]]
        
        # Convert checkbox inputs to 0 or 1
        binary_inputs = [1 if x else 0 for x in args[5:]]
        
        # Prepare the input data
        input_data = np.array([[sub_county_num] + list(args[1:5]) + binary_inputs])
        
        # Make a prediction
        prediction = model.predict(input_data)
        return np.exp(prediction[0])

# Define the Gradio interface
inputs = [
    gr.Dropdown(choices=list(subcounty_mapping.keys()), label="Sub County *"),
    gr.Slider(1, 10, step=1, label="Bedrooms *"),
    gr.Slider(1, 10, step=1, label="Bathrooms *"),
    gr.Radio([1, 0], label="Payment Type (1=Sale, 0=Rent) *"),
    gr.Radio([1, 0], label="Property Type (1=Apartment or Flat, 0=House) *"),
    gr.Checkbox(label="Swimming Pool"),
    gr.Checkbox(label="Aircon"),
    gr.Checkbox(label="Walk In Closet"),
    gr.Checkbox(label="Gated Community"),
    gr.Checkbox(label="Fibre Internet"),
    gr.Checkbox(label="Service Charge Included"),
    gr.Checkbox(label="Wheelchair Access"),
    gr.Checkbox(label="Garden"),
    gr.Checkbox(label="Golf Course"),
    gr.Checkbox(label="Scenic View"),
    gr.Checkbox(label="Staff Quarters"),
    gr.Checkbox(label="Kids Play Area"),
    gr.Checkbox(label="Gym"),
    gr.Checkbox(label="Sea View"),
    gr.Checkbox(label="BBQ"),
    gr.Checkbox(label="Alarm"),
    gr.Checkbox(label="Backup Generator"),
    gr.Checkbox(label="Borehole"),
    gr.Checkbox(label="Serviced"),
    gr.Checkbox(label="Balcony"),
    gr.Checkbox(label="Shopping Centre"),
    gr.Checkbox(label="Pet Friendly"),
    gr.Checkbox(label="Bus Stop"),
    gr.Checkbox(label="En Suite"),
    gr.Checkbox(label="CCTV"),
    gr.Checkbox(label="Electric Fence"),
    gr.Checkbox(label="Lift/Elevator"),
    gr.Checkbox(label="Furnished"),
    gr.Checkbox(label="School"),
    gr.Checkbox(label="Parking"),
    gr.Checkbox(label="Hospital"),
]

output = gr.Textbox(label="Predicted Value")

# Create the interface
gr.Interface(
    fn=predict, 
    inputs=inputs, 
    outputs=output, 
    title="Nairobi Property Price Prediction", 
    description="Enter the details of the property to predict its price."
).launch()