import numpy as np
from torch import topk, sum

import logging

logger = logging.getLogger(__name__)


def show_top_predictions(model, single_batch, top_values):
    '''
    :param model: evaluation model
    :param single_batch: single batched input for the model
    :param top_values: amount of top values to predict
    :return: dictionary of the top predictions with label as key and probability as value
    '''

    model.eval()
    prediction = model(single_batch).squeeze(0).softmax(0)

    # get top predictions of model
    probabilities, labels = topk(prediction, top_values)

    # Convert to percentages
    probabilities = probabilities * 100

    top_predictions = dict()

    for probability, label in zip(probabilities, labels):
        top_predictions[str(int(label))] = "{:.6f}".format(float(probability))

    logger.info(f"Here is the summary of the top {top_values} predictions: {top_predictions}")

    return top_predictions

def getSum_top_predictions(model, single_batch, top_values):
    '''
    :param model: evaluation model
    :param single_batch: single batched input for the model
    :param top_values: amount of top values to predict
    :return: dictionary of the top predictions with label as key and probability as value
    '''

    model.eval()
    prediction = model(single_batch).squeeze(0).softmax(0)

    # get top predictions of model
    probabilities, labels = topk(prediction, top_values)
    logger.critical(probabilities)

    # Convert to percentages
    probabilities = probabilities #* 100

    top_predictions = dict()

    top_val = float(sum(probabilities))
    top_label = np.array(labels.cpu())

    logger.info(f"TopK prediction of first {top_values} values: {top_val}")

    return top_val, top_label #round(top_val,4)
