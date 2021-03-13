# Vernaignment
Repository for Vernacular.ai assignment

## Docker commands - 
To build the docker image and to run it use the following command
- `docker-compose -f docker-compose.yml up --build`

## Docker image size - 
The size of the docker image built from the above command is - <b>84.31 MB</b>

## Note - 
- According to the docstring of `validate_finite_values_entity` we've to send the value as response if it's present in the supported_values list but in
one of the sample responses provided  `college` is not returned even if it's present in supported_values, this created some confusion so I'm sending the 
matched values if it's present in the supported values list with complaince with the docstring of the function.

<img src=./Screenshot%20from%202021-03-13%2002-28-29.png height=200 width=300>

                                  
- If there is any exceptions I'm returning a default response of 
`{
    "filled": false,
    "partially_filled": false,
    "trigger": "",
    "parameters": {}
}`

- The API's have been validated by sending POST response as form-data using Postman.
