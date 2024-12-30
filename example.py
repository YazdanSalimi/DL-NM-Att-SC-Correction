from NM_DL_ACSC import DL_inference
"""
Easy to use!
list_images is a list containing the addreess to your NIFTI input files on your machine.
model_directory is where you saved the downloaded models on your machine.
predict_directory is where you want to see your outputs
"""
list_ensmbeld_images = ensemble_regression_folds(list_images,
                                    model_directory,
                                    predict_directory,
                                    model_criteria="all",
                                    )
