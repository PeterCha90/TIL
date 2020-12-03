


# Custom Tensorflow dataset
**[Source](https://github.com/tensorflow/datasets/blob/v3.2.1/docs/add_dataset.md)**


* Simple guideline to convert local custom data into tensorflow datasets. This tutorial is written within following environments:
  
	* macOS Big Sur
  * tfds version: `v3.2.1`.


### Writing `my_dataset.py`

* #### First, install tensorflow-datasets

	```shell
    pip install tensorflow-datasets==3.2.1
    ```


* #### Second, move to where tfds installed and run the following code. In my case, the path is  `/Users/user_name/opt/anaconda3/lib/python3.7/site-packages`.

    ```shell
    cd /opt/anaconda3/lib/python3.7/site-packages
    python tensorflow_datasets/scripts/create_new_dataset.py \
      --dataset my_dataset \
      --type object_detection  # text, audio, translate,... see the flags options below.
    ```
    
	* **flags:**
      > tensorflow_datasets/scripts/create_new_dataset.py:
      > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--dataset: Dataset name
      > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--type: 						 
      >	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<audio, image, image_classification, object_detection, 
      >	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;question_answering, structured, summarization, text, translate, video>

	
* #### Third, modify the config files as other datasets written.