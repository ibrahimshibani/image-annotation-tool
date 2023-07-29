mongodb_url = "mongodb://localhost:27017/"

db_name = "supply_chain_data_factory_1"
collection_name = "deeplearning_training_images"

allowed_camera_types = ("Nikon", "Canon")
allowed_locs = ("Waldkirch Factory", "Freiburg Factory", "Stockholm Factory")
mutually_exclusive_labels = [("Envelope", "Plastic"), ("BigBox", "S"), ("BigBox", "XS")]
min_dpi = 50