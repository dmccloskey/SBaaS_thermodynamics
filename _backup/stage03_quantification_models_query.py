#LIMS
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *
#SBaaS models
from .stage03_quantification_models_postgresql_models import *
#SBaaS base
from SBaaS_base.sbaas_base import sbaas_base
#other

class stage03_quantification_models_query(sbaas_base):       
    ## Query from data_stage03_quantification_models
    # query row from data_stage03_quantification_models
    def get_row_modelID_dataStage03QuantificationModels(self,model_id_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage03_quantification_models).filter(
                    data_stage03_quantification_models.model_id.like(model_id_I)).order_by(
                    data_stage03_quantification_models.model_id.asc()).all();
            rows_O = {};
            if len(data)>1:
                print('multiple rows retrieved!');
            if data: 
                for d in data:
                    row_tmp = {'model_id':d.model_id,
                                'model_name':d.model_name,
                                'model_description':d.model_description,
                                'model_file':d.model_file,
                                'file_type':d.file_type,
                                'date':d.date};
                    rows_O.update(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    ## Query data from data_stage03_quantification_modelPathways
    # query rows from data_stage03_quantification_modelPathways
    def get_rowsDict_modelID_dataStage03QuantificationModelPathways(self,model_id_I):
        '''Query rows that are used from model pathways'''
        try:
            data = self.session.query(data_stage03_quantification_modelPathways).filter(
                    data_stage03_quantification_modelPathways.model_id.like(model_id_I),
                    data_stage03_quantification_modelPathways.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.pathway_id in rows_O:
                        print('duplicate pathway_ids found!');
                    else:
                        rows_O[d.pathway_id]={'reactions':d.reactions,
                            'stoichiometry':d.stoichiometry};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage03Models(self, data_I):
        '''add rows of data_stage03_quantification_models'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_models(d['model_id'],
                        d['model_name'],
                        d['model_description'],
                            d['model_file'],
                            d['file_type'],
                        d['date']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03Models(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_models'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_models).filter(
                            data_stage03_quantification_models.id.like(d['id'])).update(
                            {'model_id':d['model_id'],
                            'model_name':d['model_name'],
                            'model_description':d['model_description'],
                            'file':d['model_file'],
                            'file_type':d['file_type'],
                            'date':d['date']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage03ModelReactions(self, data_I):
        '''add rows of data_stage03_quantification_modelReactions'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_modelReactions(d['model_id'],
                            d['rxn_id'],
                            d['rxn_name'],
                            d['equation'],
                            d['subsystem'],
                            d['gpr'],
                            d['genes'],
                            d['reactants_stoichiometry'],
                            d['products_stoichiometry'],
                            d['reactants_ids'],
                            d['products_ids'],
                            d['lower_bound'],
                            d['upper_bound'],
                            d['objective_coefficient'],
                            d['flux_units'],
                            d['reversibility'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03ModelReactions(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_modelReactions'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_modelReactions).filter(
                            data_stage03_quantification_modelReactions.id.like(d['id'])).update(
                            {'model_id':d['model_id'],
                                'rxn_id':d['rxn_id'],
                                'rxn_name':d['rxn_name'],
                                'equation':d['equation'],
                                'subsystem':d['subsystem'],
                                'gpr':d['gpr'],
                                'genes':d['genes'],
                                'reactants_stoichiometry':d['reactants_stoichiometry'],
                                'products_stoichiometry':d['products_stoichiometry'],
                                'reactants_ids':d['reactants_ids'],
                                'products_ids':d['products_ids'],
                                'lower_bound':d['lower_bound'],
                                'upper_bound':d['upper_bound'],
                                'objective_coefficient':d['objective_coefficient'],
                                'flux_units':d['flux_units'],
                                'reversibility':d['reversibility'],
                                'used_':d['used_'],
                                'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage03ModelMetabolites(self, data_I):
        '''add rows of data_stage03_quantification_modelMetabolites'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_modelMetabolites(d['model_id'],
                        d['met_name'],
                        d['met_id'],
                        d['formula'],
                        d['charge'],
                        d['compartment'],
                        d['bound'],
                        d['constraint_sense'],
                        d['used_'],
                        d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03ModelMetabolites(self,data_I):
        '''update rows of data_stage03_quantification_modelMetabolites'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_modelMetabolites).filter(
                            data_stage03_quantification_modelMetabolites.id.like(d['id'])).update(
                            {'model_id':d['model_id'],
                                'met_name':d['met_name'],
                                'met_id':d['met_id'],
                                'formula':d['formula'],
                                'charge':d['charge'],
                                'compartment':d['compartment'],
                                'bound':d['bound'],
                                'constraint_sense':d['constraint_sense'],
                                'used_':d['used_'],
                                'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage03modelPathways(self, data_I):
        '''add rows of data_stage03_quantification_modelPathways'''
        if data_I:
            for d in data_I:
                try:
                    d['reactions'] = d['reactions'].replace(' ','');
                    d['reactions'] = d['reactions'].split(',');
                    d['stoichiometry'] = d['stoichiometry'].replace(' ','');
                    d['stoichiometry'] = numpy.array(d['stoichiometry'].split(','));
                    d['stoichiometry'] = [float(x) for x in d['stoichiometry']];
                    data_add = data_stage03_quantification_modelPathways(
                        d['model_id'],
                        d['pathway_id'],
                        d['reactions'],
                        d['stoichiometry'],
                        d['used_'],
                        d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03modelPathways(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_modelPathways'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_modelPathways).filter(
                            data_stage03_quantification_modelPathways.id.like(d['id'])).update(
                            {
                            'model_id':d['model_id'],
                            'pathway_id':d['pathway_id'],
                            'reactions':d['reactions'],
                            'stoichiometry':d['stoichiometry'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
