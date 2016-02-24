# System
import json
# SBaaS
from .stage03_quantification_dG_f_query import stage03_quantification_dG_f_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage03_quantification_dG_f_io(stage03_quantification_dG_f_query,sbaas_template_io):
            
    def import_dataStage03dGf_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage03dGf(data.data);
        data.clear_data();

    def import_dataStage03dGf_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage03dGf(data.data);
        data.clear_data();

    def import_dataStage03dG0f_add(self, filename):
        '''table adds'''
        data = base_importData();
        #data.read_csv(filename);
        data.read_json(filename);
        #data.format_data();
        self.add_dataStage03dG0f(data.data);
        #data.clear_data();

    def import_dataStage03dG0f_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage03dG0f(data.data);
        data.clear_data();
   