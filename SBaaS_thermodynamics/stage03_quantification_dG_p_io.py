# System
import json
# SBaaS
from .stage03_quantification_dG_p_query import stage03_quantification_dG_p_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage03_quantification_dG_p_io(stage03_quantification_dG_p_query):

    def import_dataStage03dGp_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage03dGp(data.data);
        data.clear_data();

    def import_dataStage03dGp_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage03dGp(data.data);
        data.clear_data();
   