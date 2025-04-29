# To test the FastAPI locally using Docker

1. Run the Docker application daemon. 
2. Run this command in shell: docker build -t microbis_ml_fastapiapp .
3. Run this command in shell: docker run -p 8000:8000 microbis_ml_fastapiapp
4a. Test the model using Swagger UI by navigating to: http://localhost:8000/docs
4b. Test the model by running this in a separate shell: 
```
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
           "model_name": "rf_8_panel_enterobac_100",
           "data": [
             {
               "Urea_hydrolysis": 0, 
               "Lactose_fermentation": 1, 
               "D-Glucose_acid": 1,
               "Citrate": 0,
               "Motility": 0,
               "Indole_production": 0,
               "Hydrogen_Sulfide_TSI": 1,
               "D-Glucose_Gas": 1
             }
           ]
         }'
```
# To test the FastAPI using EC2 instance using Docker

1. From my local machine, push the docker image to DockerHub 
2. From EC2 instance, pull the docker image and run the docker container
3. Access the FastAPI application via the EC2 instance public DNS. 