### Final Project

* Part 1. Generate sample by Captcha 

* Part 2. Verify and split the data 

* Part 3. CNN 

* Part 4. Model Training

* Part 5. Model Testing

  

##### Some instructions

* Dataset will be generated by Captcha in 'sample/'

* The model will be saved in 'model/'

* 'captcha_config.json' sets the parameters for Captcha

* 'sample_config.json' sets the parameters for our sample

  

##### CNN Structure

| Number |            Layers            |
| :----: | :--------------------------: |
| input  |            input             |
|   1    | conv + pool + dropout + ReLU |
|   2    | conv + pool + dropout + ReLU |
|   3    | conv + pool + dropout + ReLU |
|   4    |     FC + dropout + Relu      |
|   5    |         FC + softmax         |
| output |            output            |
