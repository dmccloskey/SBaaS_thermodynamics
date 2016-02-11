# System
import json
# SBaaS
from .stage03_quantification_models_query import stage03_quantification_models_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
# Dependencies from cobra
from cobra.io.sbml import create_cobra_model_from_sbml_file, write_cobra_model_to_sbml_file
from cobra.io import load_matlab_model

class stage03_quantification_models_io(stage03_quantification_models_query):

    def import_dataStage03QuantificationModel_sbml(self, model_id_I, date_I, model_sbml):
        '''import isotopomer model from file'''
        dataStage03QuantificationModelRxns_data = [];
        dataStage03QuantificationModelMets_data = [];
        dataStage03QuantificationModels_data,\
            dataStage03QuantificationModelRxns_data,\
            dataStage03QuantificationModelMets_data = self._parse_model_sbml(model_id_I, date_I, model_sbml)
        self.add_dataStage03ModelMetabolites(dataStage03QuantificationModelMets_data);
        self.add_dataStage03ModelReactions(dataStage03QuantificationModelRxns_data);
        self.add_dataStage03Models(dataStage03QuantificationModels_data);

    def import_dataStage03Models_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage03Models(data.data);
        data.clear_data();

    def import_dataStage03Models_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage03Models(data.data);
        data.clear_data();

    def import_dataStage03ModelReactions_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage03ModelReactions(data.data);
        data.clear_data();

    def import_dataStage03ModelReactions_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage03ModelReactions(data.data);
        data.clear_data();

    def import_dataStage03ModelMetabolites_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage03ModelMetabolites(data.data);
        data.clear_data();

    def import_dataStage03ModelMetabolites_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage03ModelMetabolites(data.data);
        data.clear_data();
            
    def import_dataStage03modelPathways_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage03modelPathways(data.data);
        data.clear_data();

    def import_dataStage03modelPathways_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage03modelPathways(data.data);
        data.clear_data();
   