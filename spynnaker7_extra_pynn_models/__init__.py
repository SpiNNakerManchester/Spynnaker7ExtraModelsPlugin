from spynnaker.pyNN.abstract_spinnaker_common import AbstractSpiNNakerCommon

from spynnaker_extra_pynn_models import model_binaries

# spynnaker 8 extra models
from spynnaker_extra_pynn_models.neuron.builds import IFCondExpStoc
from spynnaker_extra_pynn_models.neuron.builds import IFCurrDelta
from spynnaker_extra_pynn_models.neuron.builds import IFCurrExpCa2Adaptive

# plastic timing spynnaker 8
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    import TimingDependenceRecurrent as RecurrentRule
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    import TimingDependenceSpikeNearestPair as SpikeNearestPair
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    import TimingDependenceVogels2011 as Vogels2011Rule
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    import TimingDependencePfisterSpikeTriplet as PfisterSpikeTriplet

# plastic weight spynnaker 8
from spynnaker7_extra_pynn_models.neuron.plasticity.stdp.weight_dependence \
    import WeightDependenceAdditiveTriplet

import os

__all__ = [
    # spynnaker 7 models
    'IFCurrDelta', 'IFCurrExpCa2Adaptive', 'IFCondExpStoc',

    # spynnaker 7 plastic stuff
    'WeightDependenceAdditiveTriplet',
    'PfisterSpikeTriplet',
    'SpikeNearestPair',
    'RecurrentRule', 'Vogels2011Rule']


def _init_module():
    # import logging
    # Register this path with SpyNNaker
    AbstractSpiNNakerCommon.register_binary_search_path(
        os.path.dirname(model_binaries.__file__))


_init_module()
