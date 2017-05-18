from spynnaker_extra_pynn_models import model_binaries

# spynnaker 8 extra models
from spynnaker_extra_pynn_models.neuron.builds\
    .if_cond_exp_stoc import IFCondExpStoc
from spynnaker_extra_pynn_models.neuron.builds\
    .if_curr_delta import IFCurrDelta
from spynnaker_extra_pynn_models.neuron.builds\
    .if_curr_exp_ca2_adaptive import IFCurrExpCa2Adaptive

# plastic timing spynnaker 8
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    .timing_dependence_recurrent \
    import TimingDependenceRecurrent as RecurrentRule
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    .timing_dependence_spike_nearest_pair import \
    TimingDependenceSpikeNearestPair as SpikeNearestPair
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    .timing_dependence_vogels_2011 \
    import TimingDependenceVogels2011 as Vogels2011Rule
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    .timing_dependence_pfister_spike_triplet import \
    TimingDependencePfisterSpikeTriplet as PfisterSpikeTriplet

# plastic weight spynnaker 8
from spynnaker7_extra_pynn_models.neuron.plasticity.stdp.weight_dependence \
    .weight_dependence_additive_triplet import \
    WeightDependenceAdditiveTriplet

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
    import os
    from spynnaker.pyNN.spinnaker_common import SpiNNakerCommon

    # Register this path with SpyNNaker
    SpiNNakerCommon.register_binary_search_path(
        os.path.dirname(model_binaries.__file__))


_init_module()
