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
sys.path.append(pg_settings.datadir_settings['github']+'/thermodynamics')
sys.path.append(pg_settings.datadir_settings['github']+'/sampling')
sys.path.append(pg_settings.datadir_settings['github']+'/component-contribution')
sys.path.append(pg_settings.datadir_settings['github']+'/molmass')
sys.path.append(pg_settings.datadir_settings['github']+'/python_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/r_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/listDict')
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')

#make the measuredData table
from SBaaS_thermodynamics.stage03_quantification_measuredData_execute import stage03_quantification_measuredData_execute
exmeasuredData01 = stage03_quantification_measuredData_execute(session,engine,pg_settings.datadir_settings)
exmeasuredData01.initialize_dataStage03_quantification_measuredData();
exmeasuredData01.initialize_supportedTables();
exmeasuredData01.initialize_tables()

#make the COBRA table
from SBaaS_models.models_COBRA_execute import models_COBRA_execute
exCOBRA01 = models_COBRA_execute(session,engine,pg_settings.datadir_settings);
exCOBRA01.initialize_supportedTables();
exCOBRA01.initialize_tables()

##load '150526_iDM2015'
#exCOBRA01.import_dataStage02PhysiologyModel_json(
#    model_id_I='151026_iDM2015_irreversible',
#    date_I='2015-10-26 00:00:00',
#    model_json=pg_settings.datadir_settings['workspace_data']+ '/models/150526_iDM2015.json'
#    );

#pre-load the models
#thermomodels = exCOBRA01.get_models(model_ids_I=["iJO1366"]);
thermomodels = exCOBRA01.get_models(model_ids_I=["iJO1366_ALEWt_irreversible"]);

#make the measuredData table
from SBaaS_thermodynamics.stage03_quantification_measuredData_execute import stage03_quantification_measuredData_execute
exmeasuredData01 = stage03_quantification_measuredData_execute(session,engine,pg_settings.datadir_settings)
exmeasuredData01.initialize_supportedTables();
exmeasuredData01.initialize_tables()

##reset previous experimental data imports
#exmeasuredData01.reset_dataStage03_quantification_metabolomicsData('IndustrialStrains03');

##transfer measured metabolomics data from data_stage01_quantification_averagesMIGeo
#exmeasuredData01.execute_makeMetabolomicsData_intracellular('IndustrialStrains03');

##import exometabolomic information (i.e., media)
#exmeasuredData01.import_dataStage03QuantificationMetabolomicsData_add(
#    pg_settings.datadir_settings['workspace_data']+'/_input/170930_data_stage03_quantification_metabolomicsData_glcM901.csv');

#make the otherData table
from SBaaS_thermodynamics.stage03_quantification_otherData_execute import stage03_quantification_otherData_execute
exotherData01 = stage03_quantification_otherData_execute(session,engine,pg_settings.datadir_settings)
exotherData01.initialize_supportedTables();
exotherData01.initialize_tables()

##reset previous experimental data imports
#exotherData01.reset_dataStage03_quantification_otherData('IndustrialStrains03');

## import the pH, ionic strength, and temperature for the simulation
#exotherData01.import_dataStage03QuantificationOtherData_add(
#    pg_settings.datadir_settings['workspace_data']+'/_input/170930_data_stage03_quantification_otherData01.csv');

#make the simulatedData table
from SBaaS_thermodynamics.stage03_quantification_simulatedData_execute import stage03_quantification_simulatedData_execute
exsimData01 = stage03_quantification_simulatedData_execute(session,engine,pg_settings.datadir_settings)
exsimData01.initialize_supportedTables();
exsimData01.initialize_tables()

##reset previous experiments
#exsimData01.reset_dataStage03_quantification_simulatedData('IndustrialStrains03')

## perform FVA and single reaction deletion simulations
#exsimData01.execute_makeSimulatedData('IndustrialStrains03',models_I=thermomodels)

#make the dG_f table
from SBaaS_thermodynamics.stage03_quantification_dG_f_execute import stage03_quantification_dG_f_execute
exdGf01 = stage03_quantification_dG_f_execute(session,engine,pg_settings.datadir_settings)
exdGf01.initialize_supportedTables();
exdGf01.initialize_tables()

##reset previous dG_f adjustments
#exdGf01.reset_dataStage03_quantification_dG_f('IndustrialStrains03');

## adjust dG0 compound formation energies to the in vivo dG compound formation energies
## i.e, to the specified pH, ionic strength and temperature
#exdGf01.execute_adjust_dG_f('IndustrialStrains03',models_I=thermomodels);

#make the dG_r table
from SBaaS_thermodynamics.stage03_quantification_dG_r_execute import stage03_quantification_dG_r_execute
exdGr01 = stage03_quantification_dG_r_execute(session,engine,pg_settings.datadir_settings)
exdGr01.initialize_supportedTables();
exdGr01.initialize_tables()

## reset previous analyses
#exdGr01.reset_dataStage03_quantification_dG_r_all('IndustrialStrains03');

## calculate the in vivo dG reaction energies from adjusted dG_f and metabolomics values
## 1. dG0_r values are first calculated from the dG_f values
## 2. dG_r values are calculated from the dG0_r values and measured data
## 3. A thermodynamic consistency check is performed based on 
##    FVA, SRA, and dG_r values 
#exdGr01.execute_calculate_dG_r('IndustrialStrains03',models_I=thermomodels);

#exdGr01.reset_dataStage03_quantification_dG_r_comparison(
#    analysis_id_I='ALEsKOs01_0_evo04_0_11_evo04gnd'
#    );

##perform a thermodynamic comparison
#exdGr01.execute_compare_dG_r(
#    analysis_id_I='ALEsKOs01_0_evo04_0_11_evo04gnd',
#    simulation_id_base_I='ALEsKOs01_iJO1366_OxicEvo04EcoliGlc_0',
#    simulation_ids_I=[],
#    models_I=thermomodels,
#    measured_concentration_coverage_criteria_I=0.5,
#    measured_dG_f_coverage_criteria_I=0.99)

#make the dG_r table
from SBaaS_thermodynamics.stage03_quantification_tfba_execute import stage03_quantification_tfba_execute
tfba01 = stage03_quantification_tfba_execute(session,engine,pg_settings.datadir_settings)
tfba01.initialize_supportedTables();
tfba01.initialize_tables()

simulation_ids = ["IndustrialStrains03_iJO1366_ALEWt_irreversible_EColi_BL21_0",
"IndustrialStrains03_iJO1366_ALEWt_irreversible_EColi_C_0",
"IndustrialStrains03_iJO1366_ALEWt_irreversible_EColi_Crooks_0",
"IndustrialStrains03_iJO1366_ALEWt_irreversible_EColi_DH5a_0",
"IndustrialStrains03_iJO1366_ALEWt_irreversible_EColi_MG1655_0",
"IndustrialStrains03_iJO1366_ALEWt_irreversible_EColi_W_0",
"IndustrialStrains03_iJO1366_ALEWt_irreversible_EColi_W3110_0",
"IndustrialStrains03_iJO1366_EColi_BL21_0",
"IndustrialStrains03_iJO1366_EColi_C_0",
"IndustrialStrains03_iJO1366_EColi_Crooks_0",
"IndustrialStrains03_iJO1366_EColi_DH5a_0",
"IndustrialStrains03_iJO1366_EColi_MG1655_0",
"IndustrialStrains03_iJO1366_EColi_W_0",
"IndustrialStrains03_iJO1366_EColi_W3110_0"]

for simulation_id in simulation_ids:
    print("Running simulation_id: " + simulation_id)
    tfba01.execute_tfva(simulation_id,
        thermomodels,
        data_dir_I = '',rxn_ids_I=[],
        inconsistent_dG_f_I=[],
        inconsistent_concentrations_I=[],
        inconsistent_tcc_I=[],
        measured_concentration_coverage_criteria_I=0.5,
        measured_dG_f_coverage_criteria_I=0.99,
        solver_I='glpk')