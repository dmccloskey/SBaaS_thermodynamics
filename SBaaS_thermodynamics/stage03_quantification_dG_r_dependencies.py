#Resources
from math import copysign

class stage03_quantification_dG_r_dependencies():
    def check_significanceStatistical(self,dG_r_lb_1,dG_r_ub_1,dG_r_lb_2,dG_r_ub_2):
        '''check that the dG_r values are statistically significant
        INPUT:
        dG_r_lb_1 = Float
        dG_r_ub_1 = Float
        dG_r_lb_2 = Float
        dG_r_ub_2 = Float
        OUTPUT:
        significant_O = Boolean
        '''
        significant_O = False;
        if dG_r_ub_2 < dG_r_lb_1 or dG_r_lb_2 > dG_r_ub_1:
            significant_O = True;
        return significant_O;
    def check_significanceBiological(self,dG_r_lb_1,dG_r_ub_1,dG_r_lb_2,dG_r_ub_2):
        '''check that the dG_r values are biologically significant
        INPUT:
        dG_r_lb_1 = Float
        dG_r_ub_1 = Float
        dG_r_lb_2 = Float
        dG_r_ub_2 = Float
        OUTPUT:
        significant_O = Boolean
        '''
        significant_O = False;
        if copysign(1.0,dG_r_lb_2) != copysign(1.0,dG_r_lb_1) or copysign(1.0,dG_r_ub_2) != copysign(1.0,dG_r_ub_1):
            significant_O = True;
        return significant_O;
