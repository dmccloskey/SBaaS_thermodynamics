import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
# SBaaS paths:
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_base')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_LIMS')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_quantification')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_physiology')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_MFA')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_visualization')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_models')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_thermodynamics')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_COBRA')
# SBaaS dependencies paths:
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/quantification_analysis')
sys.path.append(pg_settings.datadir_settings['github']+'/matplotlib_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/thermodynamics/thermodynamics')
sys.path.append(pg_settings.datadir_settings['github']+'/component-contribution')
sys.path.append(pg_settings.datadir_settings['github']+'/molmass')
sys.path.append(pg_settings.datadir_settings['github']+'/python_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/r_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/listDict')
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')

#make the simulation table
from SBaaS_thermodynamics.stage03_quantification_simulation_execute import stage03_quantification_simulation_execute
exsimulation01 = stage03_quantification_simulation_execute(session,engine,pg_settings.datadir_settings);

##import the simulation parameters
#exsimulation01.import_dataStage03QuantificationSimulation_add(pg_settings.datadir_settings['workspace_data']+'/_input/141007_data_stage03_quantification_simulation.csv');
#exsimulation01.import_dataStage03QuantificationSimulationParameters_add(pg_settings.datadir_settings['workspace_data']+'/_input/141007_data_stage03_quantification_simulationParameters.csv')
#exsimulation01.import_dataStage03QuantificationSimulation_add(pg_settings.datadir_settings['workspace_data']+'/_input/151026_data_stage03_quantification_simulation01.csv');
#exsimulation01.import_dataStage03QuantificationSimulationParameters_add(pg_settings.datadir_settings['workspace_data']+'/_input/151026_data_stage03_quantification_simulationParameters01.csv')

analysis_ids = ['ALEWt01'];
simulation_ids = ['ALEWt01_iJO1366_ALEWt_irreversible_OxicEvo03Glc_0',
    'ALEWt01_iJO1366_ALEWt_irreversible_OxicEvo04Glc_0',
    'ALEWt01_iJO1366_ALEWt_irreversible_OxicEvo08Glc_0',
    'ALEWt01_iJO1366_ALEWt_irreversible_OxicEvo09Glc_0',
    'ALEWt01_iJO1366_ALEWt_irreversible_OxicWtGlc_0',
    ];
data_dir_I = 'C:/Users/dmccloskey-sbrg/Dropbox (UCSD SBRG)/MATLAB/tsampling';

#make the measuredData table
from SBaaS_thermodynamics.stage03_quantification_measuredData_execute import stage03_quantification_measuredData_execute
exmeasuredData01 = stage03_quantification_measuredData_execute(session,engine,pg_settings.datadir_settings)
exmeasuredData01.initialize_dataStage03_quantification_measuredData();

#make the COBRA table
from SBaaS_models.models_COBRA_execute import models_COBRA_execute
exCOBRA01 = models_COBRA_execute(session,engine,pg_settings.datadir_settings);
exCOBRA01.initialize_supportedTables();
exCOBRA01.initialize_COBRA_models();

#make the dG_r table
from SBaaS_thermodynamics.stage03_quantification_dG_r_execute import stage03_quantification_dG_r_execute
exdGr01 = stage03_quantification_dG_r_execute(session,engine,pg_settings.datadir_settings)
exdGr01.initialize_supportedTables();
exdGr01.initialize_tables()

#pre-load the models
thermomodels = exCOBRA01.get_models(model_ids_I=["iJO1366"]);

#perform a thermodynamic comparison
exdGr01.execute_compare_dG_r(
    analysis_id_I='ALEsKOs01_0_evo04_0_11_evo04gnd',
    simulation_id_base_I='ALEsKOs01_iJO1366_OxicEvo04EcoliGlc_0',
    simulation_ids_I=[],
    models_I=thermomodels,
    measured_concentration_coverage_criteria_I=0.5,
    measured_dG_f_coverage_criteria_I=0.99)

#make the COBRA table
from SBaaS_models.models_COBRA_execute import models_COBRA_execute
exCOBRA01 = models_COBRA_execute(session,engine,pg_settings.datadir_settings);
##reset 151026_iDM2015
#exCOBRA01.reset_COBRA_models('151026_iDM2015');
##make 151026_iDM2015
#exCOBRA01.make_modelFromRxnsAndMetsTables(
#        model_id_I='151026_iDM2015_netRxns',
#        #model_file_name_I=pg_settings.datadir_settings['workspace_data']+ '/models/150526_iDM2015.xml',
#        model_id_O='151026_iDM2015',date_O='2015-10-30 00:00:00',
#        ko_list=[],flux_dict={},
#        rxn_include_list=None,
#        description=None,
#        convert2irreversible_I=False,
#        revert2reversible_I=False,
#        convertPathway2individualRxns_I=True,
#        model_id_template_I='iJO1366_ALEWt',
#        pathway_model_id_I='iJO1366');

#test the model
#test_result = exCOBRA01.execute_testModel(model_id_I='151026_iDM2015');
#test_result = exCOBRA01.execute_testModel(model_id_I='151026_iDM2015_netRxns');
#pre-load the models
#thermomodels = exCOBRA01.get_models(model_ids_I=['151026_iDM2015']);
#test_O = exmeasuredData01.execute_testMeasuredFluxes(
#    experiment_id_I = 'ALEWt01',
#    models_I=thermomodels,
#    model_ids_I=['151026_iDM2015'],
#    diagnose_I=True);
#thermomodels = exCOBRA01.get_models(model_ids_I=['151026_iDM2015_netRxns']);
#test_O = exmeasuredData01.execute_testMeasuredFluxes(
#    experiment_id_I = 'ALEWt01',
#    models_I=thermomodels,
#    model_ids_I=['151026_iDM2015_netRxns'],
#    diagnose_I=True,
#    update_measuredFluxes_I=True,
#    adjustment_1_I=True,
#    adjustment_2_I=False,
#    );
#test_O = exmeasuredData01.execute_testMeasuredFluxes(
#    experiment_id_I = 'ALEWt01',
#    models_I=thermomodels,
#    model_ids_I=['151026_iDM2015_netRxns'],
#    diagnose_I=False,
#    update_measuredFluxes_I=False);

##151026_iDM2014
##make the tfba table
#from SBaaS_thermodynamics.stage03_quantification_tfba_execute import stage03_quantification_tfba_execute
#extfba01 = stage03_quantification_tfba_execute(session,engine,pg_settings.datadir_settings)
#extfba01.initialize_dataStage03_quantification_tfba();
#for simulation_id in simulation_ids:
#    ##reset previous simulations
#    ##extfba01.reset_dataStage03_quantification_tfba(simulation_id);
#    inconsistent_tcc=['IPDPS', 'IMPD','PPKr_reverse', 'NTD4', 'TPI', 'PGMT_reverse']
#    #load sampling points after sampling
#    extfba01.execute_analyzeThermodynamicSamplingPoints(simulation_id,
#                models_I=thermomodels,
#                data_dir_I=data_dir_I,
#                inconsistent_tcc_I=inconsistent_tcc,
#                remove_pointsNotInSolutionSpace_I=True,
#                min_pointsInSolutionSpace_I=1);
