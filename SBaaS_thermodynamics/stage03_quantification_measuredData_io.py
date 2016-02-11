# System
import json
# SBaaS
from .stage03_quantification_measuredData_query import stage03_quantification_measuredData_query
from SBaaS_quantification.stage01_quantification_averages_query import stage01_quantification_averages_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage03_quantification_measuredData_io(stage03_quantification_measuredData_query,
                                                 stage01_quantification_averages_query):
    def import_dataStage03MetabolomicsData_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage03MetabolomicsData(data.data);
        data.clear_data();

    def import_dataStage03MetabolomicsData_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage03MetabolomicsData(data.data);
        data.clear_data();
   