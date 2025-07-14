from size_lotto import size_lotto
from snr_buildN import snr_buildN
from a90_maker import a90
def localization_generator(run,t_pre_merge):
    dis=size_lotto(run)
    theta,phi,psi,I,SNRs,D=snr_buildN(t_pre_merge,dis,run)
    A90=a90(SNRs, t_pre_merge)
    return A90,theta,phi,psi,I,SNRs,dis,D
