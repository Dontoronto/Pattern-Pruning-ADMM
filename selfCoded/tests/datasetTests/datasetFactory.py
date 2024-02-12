import logging

logger = logging.getLogger(__name__)

from h5pyImageDataset import H5PYImageDataset
from torchvision.datasets import CIFAR10, CIFAR100, MNIST
import torch


@staticmethod
def kwargs_filter(kwargs, expected_keys):
    """
    Filters out the dictionary and removes unnecessary key,values
    without changing the original dictionary
    :param kwargs: -> dictionary
    :param expected_keys:  -> dictionary
    :return: -> filtered dictionary
    """
    return {k: v for k, v in kwargs.items() if k in expected_keys}



# TODO: make singleton test
class DatasetFactory:
    """
    This class is to create the right Dataset considering the structure, etc.
    Preconfigured datasets can be loaded or customized ones
    """
    @staticmethod
    #datasetName: str, storageType: str,
    #storageType == "h5py"
    def createDataset(kwargs):
        #if datasetName == 'custom':
        if kwargs['datasetName'] == "custom":
            #TODO: evtl noch für Daten in Ordnerstrukturen eigenes Dataset erstellen
            #TODO: https://github.com/pytorch/vision/blob/a52607ece94aedbe41107617ace22a8da91efc25/torchvision/datasets/folder.py#L107
            #TODO: ImageFolder klasse
            if kwargs['storageType'] == "h5py":
                expected_keys = {"root", "query", "transform"}
                logger.info("Creating Custom Dataset of h5py-file")
                return H5PYImageDataset(**kwargs_filter(kwargs,expected_keys))

        elif kwargs['datasetName'] == 'cifar10':
            logger.info("Creating preconfigured Dataset for CIFAR10")
            expected_keys = {"root","download","train","transform","target_transform"}
            return CIFAR10(**kwargs_filter(kwargs,expected_keys))

        elif kwargs['datasetName'] == 'cifar100':
            logger.info("Creating preconfigured Dataset for CIFAR100")
            expected_keys = {"root","download","train","transform","target_transform"}
            return CIFAR100(**kwargs_filter(kwargs,expected_keys))

        elif kwargs['datasetName'] == 'mnist':
            logger.info("Creating preconfigured Dataset for MNIST")
            expected_keys = {"root","download","train","transform","target_transform"}
            return MNIST(**kwargs_filter(kwargs,expected_keys))

    @staticmethod
    def updateTransformer(dataset: torch.utils.data.Dataset, transformation = None):
        if isinstance(dataset, torch.utils.data.Dataset):
            logger.info("Transformer of Dataset was changed to:")
            logger.info(transformation)
            dataset.transform = transformation
        else:
            logger.info("Given Dataset is not of type Dataset, couldn't change transform variable")

    # TODO: needs to be implemented in the future maybe
    @staticmethod
    def updateTargetTransformer():
        pass
