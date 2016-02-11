# System
import json
# SBaaS
from .stage03_quantification_simulatedData_query import stage03_quantification_simulatedData_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage03_quantification_simulatedData_io(stage03_quantification_simulatedData_query):
            
    def import_dataStage03SimulatedData_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage03SimulatedData(data.data);
        data.clear_data();

    def import_dataStage03SimulatedData_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage03SimulatedData(data.data);
        data.clear_data();
   