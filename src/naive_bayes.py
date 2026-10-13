"""Bayes' rule, and naive Bayes built on top of it.

**You implement four functions in this file**: `bayes_rule`, `train`,
`classify` and `accuracy`. Everything else is provided.

The tables are plain dictionaries:

    distribution   class -> probability
                   {"present": 0.3, "absent": 0.7}

    likelihood     class -> P(this one observation | class)
                   {"present": 0.85, "absent": 0.10}

    example        a class and the evidence seen with it
                   ("present", {"camera": "yes", "lidar": "no"})

A trained `Model` holds a prior, P(class), and a likelihood table for every
feature, value and class: `model.likelihood["camera"]["yes"]["present"]` is
P(camera = yes | present).

None of these functions knows anything about cars or pedestrians. They work
for any classes and any features, which the tests check.
"""

from typing import NamedTuple

Distribution = dict[str, float]
Evidence = dict[str, str]
Example = tuple[str, Evidence]


class Model(NamedTuple):
    """A trained naive Bayes model."""

    prior: Distribution
    likelihood: dict[str, dict[str, Distribution]]


def bayes_rule(prior: Distribution, likelihood: Distribution) -> Distribution:
    """Return the posterior after one observation, by Bayes' rule.

    Multiply each class's prior by the likelihood of the observation under
    that class, then divide every product by their sum. The sum is the
    probability of the observation, by the law of total probability. Return
    a new dictionary; do not change `prior`.

    Args:
        prior: P(class) for each class.
        likelihood: P(observation | class) for each class.

    Returns:
        P(class | observation) for each class.
    """
    # TODO: implement this
    raise NotImplementedError


def train(examples: list[Example], smoothing: float = 1.0) -> Model:
    """Return a naive Bayes model learned by counting the examples.

    The prior P(c) is the share of examples in class c. For each feature, the
    likelihood P(feature = v | c) is the share of class-c examples where the
    feature has value v, with `smoothing` added to every count:

        P(feature = v | c) = (count(v, c) + smoothing) /
                             (count(c) + smoothing * number of values)

    The values of a feature are every value it takes anywhere in the
    examples. With smoothing 0 the likelihoods are plain shares.

    Args:
        examples: Labelled examples, each a class and its evidence.
        smoothing: The number added to every count. 1 by default.

    Returns:
        The prior and the likelihood tables.
    """
    # TODO: implement this
    raise NotImplementedError


def classify(model: Model, evidence: Evidence) -> Distribution:
    """Return P(class | evidence) by naive Bayes.

    For each class, multiply its prior by P(feature = value | class) for every
    feature in the evidence. Then divide every product by their sum. A
    feature the model has no table for is skipped.

    Args:
        model: A trained model.
        evidence: The observed value of some or all features.

    Returns:
        P(class | evidence) for each class.
    """
    # TODO: implement this
    raise NotImplementedError


def accuracy(model: Model, examples: list[Example]) -> float:
    """Return the share of examples whose most likely class is their label.

    Args:
        model: A trained model.
        examples: Labelled examples to test on.

    Returns:
        A number from 0 to 1.
    """
    # TODO: implement this
    raise NotImplementedError
