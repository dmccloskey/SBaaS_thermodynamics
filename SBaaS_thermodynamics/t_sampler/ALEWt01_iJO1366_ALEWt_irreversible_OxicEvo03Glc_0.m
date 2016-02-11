% initialize with Tomlab_CPLEX
load('t_sampler/ALEWt01_iJO1366_ALEWt_irreversible_OxicEvo03Glc_0.mat')
initCobraToolbox();
% sample
[sampler_out, mixedFrac] = gpSampler(iJO1366, [], [], 20000, [], [], true);
[sampler_out, mixedFrac] = gpSampler(sampler_out, [], [], 20000, [], [], true);
save('t_sampler/ALEWt01_iJO1366_ALEWt_irreversible_OxicEvo03Glc_0_points.mat','sampler_out', 'mixedFrac');