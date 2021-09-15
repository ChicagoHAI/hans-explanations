"""
Reads csv file with templates and fill in 1 generated example for each template
"""
import csv 
import random
import os
import sys
import math

vocab_split_setting = -1

Ns = []
Np = []
N = []
Vt = []
Vi = []
V = []
P = []
Adj = []
Adv = []
Rels = []
Vunderstand = []
called_objects = []
told_objects = []
food_words = []
location_nouns = []
location_nouns_b = []
won_objects = []
read_wrote_objects = []
Vpp = []
Nlocation = []
Conj = []
Vnpz = []
Vnps = []
Vconstquotentailed = []
Advoutent = []
Advent = []
Advembent = []
Advoutnent = []
Vnonentquote = []
Advnonent = []
Advembnent = []
var_of_string = None

Ns_ind = []
Np_ind = []
N_ind = []
Vt_ind = []
Vi_ind = []
V_ind = []
P_ind = []
Adj_ind = []
Adv_ind = []
Rels_ind = []
Vunderstand_ind = []
called_objects_ind = []
told_objects_ind = []
food_words_ind = []
location_nouns_ind = []
location_nouns_b_ind = []
won_objects_ind = []
read_wrote_objects_ind = []
Vpp_ind = []
Nlocation_ind = []
Conj_ind = []
Vnpz_ind = []
Vnps_ind = []
Vconstquotentailed_ind = []
Advoutent_ind = []
Advent_ind = []
Advembent_ind = []
Advoutnent_ind = []
Vnonentquote_ind = []
Advnonent_ind = []
Advembnent_ind = []

Ns_ood = []
Np_ood = []
N_ood = []
Vt_ood = []
Vi_ood = []
V_ood = []
P_ood = []
Adj_ood = []
Adv_ood = []
Rels_ood = []
Vunderstand_ood = []
called_objects_ood = []
told_objects_ood = []
food_words_ood = []
location_nouns_ood = []
location_nouns_b_ood = []
won_objects_ood = []
read_wrote_objects_ood = []
Vpp_ood = []
Nlocation_ood = []
Conj_ood = []
Vnpz_ood = []
Vnps_ood = []
Vconstquotentailed_ood = []
Advoutent_ood = []
Advent_ood = []
Advembent_ood = []
Advoutnent_ood = []
Vnonentquote_ood = []
Advnonent_ood = []
Advembnent_ood = []

var_type_subtypes={
    "N": ["Np", "Ns", "Nlocation"],
    "V": ["Vt", "Vi", "Vunderstand", "Vpp", "Vnpz", "Vnps", "Vconstquotentailed", "Vnonentquote"],
    "Adj": [],
    "Adv": ['Advoutent', 'Advent', 'Advembent', 'Advoutnent', 'Advnonent', 'Advembnent'],
    "Be": ['BePast'],
    "P": [],
    "Rels": [],
    "O": [],
    "Conj": [],
}

Ns_all=["professor", "student", "president","judge","senator","programmer","doctor","lawyer","scientist","banker","tourist","manager","artist","author","actor","athlete", \
    "designer", "animator", "architect", "administrator", "artisan", "therapist", "baker", "artist", "officer", \
    "colorist", "curator", "dancer", "director", "strategist", "essayist", "planner", "stylist", "illustrator", "lyricist", \
    "musician", "penciller", "photographer", "photojournalist", "potter", "sculptor", "singer", "writer", \
    "chaplain", "analyst", "counselor", "nurse", "psychiatrist", "psychologist", "psychotherapist", "worker", "engineer", \
    "technologist", "technician"]
Np_all=["professors", "students", "presidents","judges","senators","programmers","doctors","lawyers","scientists","bankers","tourists","managers","artists","authors","actors","athletes", \
    "designers", "animators", "architects", "administrators", "artisans", "therapists", "bakers", "artists", "officers", \
    "colorists", "curators", "dancers", "directors", "strategists", "essayists", "planners", "stylists", "illustrators", "lyricists", \
    "musicians", "pencillers", "photographers", "photojournalists", "potters", "sculptors", "singers", "writers", \
    "chaplains", "analysts", "counselors", "nurses", "psychiatrists", "psychologists", "psychotherapists", "workers", "engineers", \
    "technologists", "technicians"]
N_all=Np_all+Ns_all

Vt_all=["recommended", "called", "helped","supported","contacted","avoided","advised","saw","introduced","mentioned","encouraged","thanked", \
    "recognized","admired", "addressed", "needed", "brought", "disturbed", "deceived", "offended", "affected", "found", "expected"]
Vi_all=["slept", "danced", "ran","shouted","resigned","waited", "arrived", "performed", \
    "voted", "sat", "laughed", "agreed", "appeared", "continued", "cried", "died", "existed", "grew", "lay", "listened", "panicked", "smiled", \
    "talked", "worked", "yelled"]
V_all=Vi_all+Vt_all

P_all=["near", "behind", "by", "in front of", "next to"]

Adj_all = ["important", "popular", "famous", "young", "happy", "helpful", "serious", "angry", \
       "ambitious", "agreeable", "angry", "thoughtless", "obedient", "reliable", "witty", "silly", "gentle", "compassionate", "lazy", "nervous"]

Adv_all = ["quickly", "slowly", "happily", "easily", "quietly", "thoughtfully", \
       "anxiously", "arrogantly", "awkwardly", "bashfully", "bitterly", "blindly", "blissfully", "boastfully", "boldly", "bravely", "briefly", "brightly", "briskly", \
       "broadly", "busily", "calmly", "carefully", "carelessly", "cautiously", "certainly", "cheerfully"]

Rels_all = ["that", "who"]

Vunderstand_all = ["paid", "explored", "won", "wrote", "left", "read", "ate"]
called_objects_all = ["coward", "liar", "hero", "fool"]
told_objects_all = ["story", "lie", "truth", "secret"]
food_words_all = ["fruit", "salad", "broccoli", "sandwich", "rice", "corn", "ice cream"]
location_nouns_all = ["neighborhood", "region", "country", "town", "valley", "forest", "garden", "museum", "desert", "island", "town"]
location_nouns_b_all = ["museum", "school", "library", "office","laboratory"]
won_objects_all = ["race", "contest", "war", "prize", "competition", "election", "battle", "award", "tournament"]
read_wrote_objects_all = ["book", "column", "report", "poem", "letter", "novel", "story", "play", "speech"]

Vunderstand_object_dict = {}
Vunderstand_object_dict["called"] = called_objects_all
Vunderstand_object_dict["told"] = told_objects_all
Vunderstand_object_dict["brought"] = food_words_all
Vunderstand_object_dict["made"] = food_words_all
Vunderstand_object_dict["saved"] = food_words_all
Vunderstand_object_dict["offered"] = food_words_all
Vunderstand_object_dict["explored"] = location_nouns_all
Vunderstand_object_dict["won"] = won_objects_all
Vunderstand_object_dict["wrote"] = read_wrote_objects_all
Vunderstand_object_dict["left"] = location_nouns_all
Vunderstand_object_dict["read"] = read_wrote_objects_all
Vunderstand_object_dict["ate"] = food_words_all
Vunderstand_object_dict["paid"] = N_all

Vpp_all = ["studied", "paid", "helped","investigated", "presented"]
Nlocation_all = ["museum", "school", "library", "office","laboratory"]

Conj_all = ["while", "after", "before", "when", "although", "because", "since"]
Vnpz_all = ["hid", "moved", "presented", "paid","studied","stopped", "fought"]
Vnps_all = ["believed", "knew", "heard"]
Vconstquotentailed_all = ["forgot", "learned", "remembered", "knew"]

Advoutent_all = ["after", "before", "because", "although", "though", "since", "while"]
Advent_all = ["certainly", "definitely", "clearly", "obviously", "suddenly"]
Advembent_all = ["after", "before", "because", "although", "though", "since", "while"]
Advoutnent_all = ["if", "unless"]
Vnonentquote_all = ["hoped", "claimed", "thought", "believed", "said", "assumed"]
Advnonent_all = ["supposedly", "probably", "maybe", "hopefully"]
Advembnent_all = ["if","unless"]


def split_in_half(alist, by_abundance=False):
    if by_abundance == True and len(alist) < 4:
        return alist, alist
    else:
        random.shuffle(alist)
        desired_length = math.floor(len(alist)/2)
        return alist[:desired_length], alist[desired_length:]


def ind_ood_split():
    global Ns_ind
    global Np_ind
    global N_ind
    global Vt_ind
    global Vi_ind
    global V_ind
    global P_ind
    global Adj_ind
    global Adv_ind
    global Rels_ind
    global Vunderstand_ind
    global called_objects_ind
    global told_objects_ind
    global food_words_ind
    global location_nouns_ind
    global location_nouns_b_ind
    global won_objects_ind
    global read_wrote_objects_ind
    global Vpp_ind
    global Nlocation_ind
    global Conj_ind
    global Vnpz_ind
    global Vnps_ind
    global Vconstquotentailed_ind
    global Advoutent_ind
    global Advent_ind
    global Advembent_ind
    global Advoutnent_ind
    global Vnonentquote_ind
    global Advnonent_ind
    global Advembnent_ind

    global Ns_ood
    global Np_ood
    global N_ood
    global Vt_ood
    global Vi_ood
    global V_ood
    global P_ood
    global Adj_ood
    global Adv_ood
    global Rels_ood
    global Vunderstand_ood
    global called_objects_ood
    global told_objects_ood
    global food_words_ood
    global location_nouns_ood
    global location_nouns_b_ood
    global won_objects_ood
    global read_wrote_objects_ood
    global Vpp_ood
    global Nlocation_ood
    global Conj_ood
    global Vnpz_ood
    global Vnps_ood
    global Vconstquotentailed_ood
    global Advoutent_ood
    global Advent_ood
    global Advembent_ood
    global Advoutnent_ood
    global Vnonentquote_ood
    global Advnonent_ood
    global Advembnent_ood

    Ns_ind, Ns_ood = split_in_half(Ns_all)
    Np_ind = [elt+"s" for elt in Ns_ind] #add s to words in nouns_sg_train
    Np_ood = [elt+"s" for elt in Ns_ood] #add s to words in nouns_sg_test
    N_ind= Ns_ind + Np_ind
    N_ood = Ns_ood + Np_ood

    Vt_ind, Vt_ood = split_in_half(Vt_all)
    Vi_ind, Vi_ood = split_in_half(Vi_all)
    V_ind = Vt_ind + Vi_ind
    V_ood = Vt_ood + Vi_ood
    
    Adj_ind, Adj_ood = split_in_half(Adj_all)
    Adv_ind, Adv_ood = split_in_half(Adv_all)

    global vocab_split_setting
    if vocab_split_setting == 1:
        P_ind, P_ood = split_in_half(P_all)
        Rels_ind, Rels_ood = split_in_half(Rels_all)
        Vunderstand_ind, Vunderstand_ood = split_in_half(Vunderstand_all)
        called_objects_ind, called_objects_ood = split_in_half(called_objects_all)
        told_objects_ind, told_objects_ood = split_in_half(told_objects_all)
        food_words_ind, food_words_ood = split_in_half(food_words_all)
        location_nouns_ind, location_nouns_ood = split_in_half(location_nouns_all)
        location_nouns_b_ind, location_nouns_b_ood = split_in_half(location_nouns_b_all)
        won_objects_ind, won_objects_ood = split_in_half(won_objects_all)
        read_wrote_objects_ind, read_wrote_objects_ood = split_in_half(read_wrote_objects_all)
        Vpp_ind, Vpp_ood = split_in_half(Vpp_all)
        Nlocation_ind, Nlocation_ood = split_in_half(Nlocation_all)
        Conj_ind, Conj_ood = split_in_half(Conj_all)
        Vnpz_ind, Vnpz_ood = split_in_half(Vnpz_all)
        Vnps_ind, Vnps_ood = split_in_half(Vnps_all)
        Vconstquotentailed_ind, Vconstquotentailed_ood = split_in_half(Vconstquotentailed_all)
        Advoutent_ind, Advoutent_ood = split_in_half(Advoutent_all)
        Advent_ind, Advent_ood = split_in_half(Advent_all)
        Advembent_ind, Advembent_ood = split_in_half(Advembent_all)
        Advoutnent_ind, Advoutnent_ood = split_in_half(Advoutnent_all)
        Vnonentquote_ind, Vnonentquote_ood = split_in_half(Vnonentquote_all)
        Advnonent_ind, Advnonent_ood = split_in_half(Advnonent_all)
        Advembnent_ind, Advembnent_ood = split_in_half(Advembnent_all)
    elif vocab_split_setting == 2:
        P_ind = P_ood = P_all
        Rels_ind = Rels_ood = Rels_all
        Vunderstand_ind = Vunderstand_ood = Vunderstand_all
        called_objects_ind = called_objects_ood = called_objects_all
        told_objects_ind = told_objects_ood = told_objects_all
        food_words_ind = food_words_ood = food_words_all
        location_nouns_ind = location_nouns_ood = location_nouns_all
        location_nouns_b_ind = location_nouns_b_ood = location_nouns_b_all
        won_objects_ind = won_objects_ood = won_objects_all
        read_wrote_objects_ind = read_wrote_objects_ood = read_wrote_objects_all
        Vpp_ind = Vpp_ood = Vpp_all
        Nlocation_ind = Nlocation_ood = Nlocation_all
        Conj_ind = Conj_ood = Conj_all
        Vnpz_ind = Vnpz_ood = Vnpz_all
        Vnps_ind = Vnps_ood = Vnps_all
        Vconstquotentailed_ind = Vconstquotentailed_ood = Vconstquotentailed_all
        Advoutent_ind = Advoutent_ood = Advoutent_all
        Advent_ind = Advent_ood = Advent_all
        Advembent_ind = Advembent_ood = Advembent_all
        Advoutnent_ind = Advoutnent_ood = Advoutnent_all
        Vnonentquote_ind = Vnonentquote_ood = Vnonentquote_all
        Advnonent_ind = Advnonent_ood = Advnonent_all
        Advembnent_ind = Advembnent_ood = Advembnent_all
    elif vocab_split_setting == 3:
        P_ind, P_ood = split_in_half(P_all, by_abundance = True)
        Rels_ind, Rels_ood = split_in_half(Rels_all, by_abundance = True)
        Vunderstand_ind, Vunderstand_ood = split_in_half(Vunderstand_all, by_abundance = True)
        called_objects_ind, called_objects_ood = split_in_half(called_objects_all, by_abundance = True)
        told_objects_ind, told_objects_ood = split_in_half(told_objects_all, by_abundance = True)
        food_words_ind, food_words_ood = split_in_half(food_words_all, by_abundance = True)
        location_nouns_ind, location_nouns_ood = split_in_half(location_nouns_all, by_abundance = True)
        location_nouns_b_ind, location_nouns_b_ood = split_in_half(location_nouns_b_all, by_abundance = True)
        won_objects_ind, won_objects_ood = split_in_half(won_objects_all, by_abundance = True)
        read_wrote_objects_ind, read_wrote_objects_ood = split_in_half(read_wrote_objects_all, by_abundance = True)
        Vpp_ind, Vpp_ood = split_in_half(Vpp_all, by_abundance = True)
        Nlocation_ind, Nlocation_ood = split_in_half(Nlocation_all, by_abundance = True)
        Conj_ind, Conj_ood = split_in_half(Conj_all, by_abundance = True)
        Vnpz_ind, Vnpz_ood = split_in_half(Vnpz_all, by_abundance = True)
        Vnps_ind, Vnps_ood = split_in_half(Vnps_all, by_abundance = True)
        Vconstquotentailed_ind, Vconstquotentailed_ood = split_in_half(Vconstquotentailed_all, by_abundance = True)
        Advoutent_ind, Advoutent_ood = split_in_half(Advoutent_all, by_abundance = True)
        Advent_ind, Advent_ood = split_in_half(Advent_all, by_abundance = True)
        Advembent_ind, Advembent_ood = split_in_half(Advembent_all, by_abundance = True)
        Advoutnent_ind, Advoutnent_ood = split_in_half(Advoutnent_all, by_abundance = True)
        Vnonentquote_ind, Vnonentquote_ood = split_in_half(Vnonentquote_all, by_abundance = True)
        Advnonent_ind, Advnonent_ood = split_in_half(Advnonent_all, by_abundance = True)
        Advembnent_ind, Advembnent_ood = split_in_half(Advembnent_all, by_abundance = True)

    
def set_vocab_by_type(data_type):
    # data_type can be either "ind" or "ood" 
    global Ns
    global Np
    global N
    global Vt
    global Vi
    global V
    global P 
    global Adj 
    global Adv 
    global Rels 
    global Vunderstand 
    global called_objects 
    global told_objects 
    global food_words
    global location_nouns 
    global location_nouns_b 
    global won_objects
    global read_wrote_objects 
    global Vpp 
    global Nlocation 
    global Conj 
    global Vnpz 
    global Vnps 
    global Vconstquotentailed 
    global Advoutent 
    global Advent 
    global Advembent 
    global Advoutnent 
    global Vnonentquote 
    global Advnonent 
    global Advembnent 
    global Vunderstand_object_dict
    global var_of_string

    if data_type == "ind":
        Ns = Ns_ind
        Np = Np_ind
        N = N_ind
        Vt = Vt_ind
        Vi = Vi_ind
        V = V_ind
        P = P_ind
        Adj = Adj_ind
        Adv = Adv_ind
        Rels = Rels_ind
        Vunderstand = Vunderstand_ind
        called_objects = called_objects_ind
        told_objects = told_objects_ind
        food_words = food_words_ind
        location_nouns = location_nouns_ind
        location_nouns_b = location_nouns_b_ind
        won_objects = won_objects_ind
        read_wrote_objects = read_wrote_objects_ind
        Vpp = Vpp_ind
        Nlocation = Nlocation_ind
        Conj = Conj_ind
        Vnpz = Vnpz_ind
        Vnps = Vnps_ind
        Vconstquotentailed = Vconstquotentailed_ind
        Advoutent = Advoutent_ind
        Advent = Advent_ind
        Advembent = Advembent_ind
        Advoutnent = Advoutnent_ind
        Vnonentquote = Vnonentquote_ind
        Advnonent = Advnonent_ind
        Advembnent = Advembnent_ind

        # update Vunderstand_object_dict
        Vunderstand_object_dict["called"] = called_objects
        Vunderstand_object_dict["told"] = told_objects
        Vunderstand_object_dict["brought"] = food_words
        Vunderstand_object_dict["made"] = food_words
        Vunderstand_object_dict["saved"] = food_words
        Vunderstand_object_dict["offered"] = food_words
        Vunderstand_object_dict["explored"] = location_nouns
        Vunderstand_object_dict["won"] = won_objects
        Vunderstand_object_dict["wrote"] = read_wrote_objects
        Vunderstand_object_dict["left"] = location_nouns
        Vunderstand_object_dict["read"] = read_wrote_objects
        Vunderstand_object_dict["ate"] = food_words
        Vunderstand_object_dict["paid"] = N

    elif data_type == "ood":
        Ns = Ns_ood
        Np = Np_ood
        N = N_ood
        Vt = Vt_ood
        Vi = Vi_ood
        V = V_ood
        P = P_ood
        Adj = Adj_ood
        Adv = Adv_ood
        Rels = Rels_ood
        Vunderstand = Vunderstand_ood
        called_objects = called_objects_ood
        told_objects = told_objects_ood
        food_words = food_words_ood
        location_nouns = location_nouns_ood
        location_nouns_b = location_nouns_b_ood
        won_objects = won_objects_ood
        read_wrote_objects = read_wrote_objects_ood
        Vpp = Vpp_ood
        Nlocation = Nlocation_ood
        Conj = Conj_ood
        Vnpz = Vnpz_ood
        Vnps = Vnps_ood
        Vconstquotentailed = Vconstquotentailed_ood
        Advoutent = Advoutent_ood
        Advent = Advent_ood
        Advembent = Advembent_ood
        Advoutnent = Advoutnent_ood
        Vnonentquote = Vnonentquote_ood
        Advnonent = Advnonent_ood
        Advembnent = Advembnent_ood

        # update Vunderstand_object_dict
        Vunderstand_object_dict["called"] = called_objects
        Vunderstand_object_dict["told"] = told_objects
        Vunderstand_object_dict["brought"] = food_words
        Vunderstand_object_dict["made"] = food_words
        Vunderstand_object_dict["saved"] = food_words
        Vunderstand_object_dict["offered"] = food_words
        Vunderstand_object_dict["explored"] = location_nouns
        Vunderstand_object_dict["won"] = won_objects
        Vunderstand_object_dict["wrote"] = read_wrote_objects
        Vunderstand_object_dict["left"] = location_nouns
        Vunderstand_object_dict["read"] = read_wrote_objects
        Vunderstand_object_dict["ate"] = food_words
        Vunderstand_object_dict["paid"] = N

    else:
        print("Wrong data type!")

    var_of_string={
        "N": N,
        "Ns": Ns,
        "Np": Np,
        "V": V,
        "Vt": Vt,
        "Vi": Vi,
        "Adj": Adj,
        "Adv": Adv,
        "P": P,
        "Rels": Rels,
        "Vunderstand": Vunderstand,
        "VunderstandO": Vunderstand_object_dict,
        "Vpp": Vpp,
        "Vnonentquote": Vnonentquote,
        "Nlocation": Nlocation,
        "Conj": Conj,
        "Vnpz": Vnpz,
        "Vnps": Vnps,
        "Vconstquotentailed": Vconstquotentailed,
        "Advoutent": Advoutent,
        "Advent": Advent,
        "Advembent": Advembent,
        "Advoutnent": Advoutnent,
        "Advnonent": Advnonent,
        "Advembnent": Advembnent,
    }


class Variable:
    def __init__(self, variable_name, variable_index, variable_type, variable_subtype=None, variable_association=None):
        self.name=variable_name # e.g. N1, Np2, etc.
        self.index=variable_index # index for the n-th variable of the same type in the template
        self.type=variable_type # e.g. N, V, etc.
        self.subtype=variable_subtype # e.g. Vi, Vt, Np, Ns etc.
        self.association=variable_association # e.g. N1_BE1 has association N1
        self.check()
    
    def check(self):
        # check Be to have associated nouns
        if self.type=='Be' and self.association==None:
            print('error: variable Be needs to have an associated noun')

    def set_value(self, value):
        self.value=value


class Template:
    def __init__(self, csv_id, heuristic, template, subtemplate_id, label, premise, hypothesis, \
                 high_quality, extreme_low_quality, var_list):
        self.id=csv_id # id in templates.csv, used for debugging purpose only
        self.heuristic=heuristic 
        self.template=template
        self.subtemplate_id=subtemplate_id
        self.label=label
        if label[0] == ' ':
            self.label=label[1:]
        self.premise=premise
        self.hypothesis=hypothesis
        self.high_quality=high_quality
        self.extreme_low_quality=extreme_low_quality
        self.var_list=eval(var_list) 
        self.variable_dict = dict((var_name, self.get_variable(var_name)) for var_name in self.var_list)

    def generate_one_example(self):
        self._sample_words()
        self._get_one_example_for_all()
        return self.output()

    def get_variable(self, var):
        variable_name, variable_index, variable_type, variable_subtype, variable_association = parse_variable(var)
        return Variable(variable_name, variable_index, variable_type, variable_subtype, variable_association)
        
    def _sample_words(self):
        """ sample word for each variable in variable_dict.values(), check for dups for each var type """
        sampled_nouns = set()
        sampled_verbs = set()
        sampled_dict={'N': sampled_nouns, 'V': sampled_verbs}
        
        for variable in self.variable_dict.values():
            value=None
            if variable.type in ['Be', 'O']:
                continue
            if variable.type in ['V', 'N']:
                have_value=False
                while contains_dup(sampled_dict[variable.type], value) or not have_value:
                    if variable.subtype != None:
                        value = random.sample(var_of_string[variable.subtype],1)[0]
                        have_value = True
                    else:
                        value = random.sample(var_of_string[variable.type],1)[0]
                        have_value = True
                sampled_dict[variable.type].add(value)
            
            else:
                if variable.subtype == None:
                    value = random.sample(var_of_string[variable.type],1)[0]
                else:
                    value = random.sample(var_of_string[variable.subtype],1)[0]
            variable.set_value(value)
        # decide Be after sampling all nouns
        for variable in self.variable_dict.values():
            if variable.type=='Be':
                association = variable.association
                for v in self.variable_dict.values():
                    if v.name == association:
                        if v.subtype == 'Np':
                            if variable.subtype == 'BePast': 
                                variable.set_value('were')
                            else:
                                variable.set_value('are')
                        elif v.subtype == 'Ns':
                            if variable.subtype == 'BePast': 
                                variable.set_value('was')
                            else:
                                variable.set_value('is')
                        else: #N
                            if v.value[-1]=='s':
                                if variable.subtype == 'BePast': 
                                    variable.set_value('were')
                                else:
                                    variable.set_value('are')
                            else:
                                if variable.subtype == 'BePast': 
                                    variable.set_value('was')
                                else:
                                    variable.set_value('is')
                        break
            elif variable.type=="O":
                association = variable.association
                for v in self.variable_dict.values():
                    if v.name == association:
                        dictionary = var_of_string[v.subtype+'O']
                        O_list = dictionary[v.value]
                        value = random.sample(O_list,1)[0]
                        variable.set_value(value)
                
    def _get_one_example_for_all(self):
        """ fill word in for the examples and output for p, h, and different expls """
        # premise
        self.example_premise = self._get_one_example(self.premise)
        # hypotheis
        self.example_hypotheis = self._get_one_example(self.hypothesis)
        # high_quality
        self.example_high_quality = self._get_one_example(self.high_quality)
        # extreme_low_quality
        self.example_extreme_low_quality = self._get_one_example(self.extreme_low_quality)

    def _get_one_example(self, template):
        has_period = False
        if template[-1] =='.':
            holder = template[:-1]
            has_period = True
        else:
            holder = template
        template_t_list = holder.split()
        example_t_list = [t if t not in self.variable_dict.keys() else self.variable_dict[t].value for t in template_t_list] 
        
        if has_period: example_t_list.append('.')
        return ' '.join(example_t_list)

    def output(self):
        """
        output in a list for the output csv row format
        """
        return [self.id, self.heuristic, self.template, self.subtemplate_id, self.label, self.premise, self.hypothesis, \
                self.high_quality, self.extreme_low_quality, self.var_list, \
                self.example_premise, self.example_hypotheis, self.example_high_quality, \
                self.example_extreme_low_quality]
        

def contains_dup(word_set, word):
    """ checks if word has singular/plural form in word_set """
    if word in word_set:
        return True
    elif word in Ns:
        if word+"s" in word_set:
            return True
    elif word in Np:
        if word[:-1] in word_set:
            return True
    else:
        return False


def parse_variable(var):
    var_name = var
    # association
    var_association = None
    association_var = var.split('_')
    if len(association_var) == 2:
        var_association = association_var[0]
        var = association_var[1]
    elif len(association_var) == 1:
        var = association_var[0]
    else:
        print('error: too many _ in variable name')
    # index
    var_index = var[-1]
    var=var[:-1]
    # type and subtype
    var_type = None
    var_subtype = None
    if var in var_type_subtypes.keys():
        var_type = var
    else:
        var_subtype = var
        for k, v in var_type_subtypes.items(): 
            if var_subtype in v:
                var_type = k
        if var_type==None:
            var_subtype=None
    return var_name, var_index, var_type, var_subtype, var_association


def read_templates(fi):
    """
    input: 
    fi: file path

    output:
    a list of Template objects 
    """
    templates = []
    with open(fi) as f:
        reader = csv.reader(f)
        for (i, line) in enumerate(reader):
            if i > 0:
                template = Template(line[0], line[1], line[2], line[3], line[4], line[5], line[6], \
                                    line[7], line[8], line[9])
                templates.append(template)
    return templates


def filter_by_template_partition(template_partition, output_rows):
    '''
    template_partition: list of template ids
    output_rows[1] = template_id
    '''
    filtered_result = []
    for row in output_rows:
        if eval(row[1]) in template_partition:
            filtered_result.append(row)
    return filtered_result


def get_train_dev_test_partitions(partitions, partition_index):
    test_partition = partitions[partition_index]

    train_dev_partitions = partitions[:partition_index] + partitions[partition_index+1:]
    train_dev_partition = []
    for p in train_dev_partitions:
        train_dev_partition.extend(p)

    return train_dev_partition, test_partition


def write_csv(filename, data, fieldnames):
    '''
    data is a 2-D list, each item in each list correspond to value of one key in the fieldnames 
    '''
    with open(filename, 'w+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            data_dict = {}
            for i in range(len(fieldnames)):
                data_dict[fieldnames[i]] = item[i]
            writer.writerow(data_dict)


def get_ood_data(templates, train_dev_partition, test_partition, fo_test_ovit, fo_test_ovot, output_header):
    set_vocab_by_type('ood')
    num_examples = 300
    output_rows = []
    guid = 0
    for t in templates:
        existing_templates = []
        for i in range(num_examples):
            generated_template = t.generate_one_example()
            
            # check generated_template duplicate with existing
            while generated_template in existing_templates:
                generated_template = t.generate_one_example()
            
            # add guid
            output_rows.append([guid]+generated_template)
            guid += 1
            existing_templates.append(generated_template)

    # filter by templates partitions
    output_rows_test_ovit = filter_by_template_partition(train_dev_partition, output_rows)
    output_rows_test_ovot = filter_by_template_partition(test_partition, output_rows)
    write_csv(fo_test_ovit, output_rows_test_ovit, output_header)
    write_csv(fo_test_ovot, output_rows_test_ovot, output_header)


def get_ind_data(templates, train_dev_partition, test_partition, fo_dir, fo_train, fo_dev, fo_test_ivit, fo_test_ivot, output_header):
    set_vocab_by_type('ind')
    num_examples = 492
    output_rows_train = []
    output_rows_dev = []
    output_rows_test = []
    guid_train = 0
    guid_dev = 0
    guid_test = 0
    output_rows_train_by_template = {}
    output_rows_dev_by_template = {}
    for t in templates:
        existing_templates = []
        for i in range(num_examples):
            generated_template = t.generate_one_example()
            
            # check generated_template duplicate with existing
            while generated_template in existing_templates:
                generated_template = t.generate_one_example()
            
            # add guid
            if i < 160:
                line = [guid_train]+generated_template
                template_id = generated_template[0]
                if template_id in output_rows_train_by_template:
                    output_rows_train_by_template[template_id].append(line)
                else:
                    output_rows_train_by_template[template_id] = [line]
                output_rows_train.append(line)
                guid_train += 1
            elif i < 192:
                line = [guid_dev]+generated_template
                template_id = generated_template[0]
                if template_id in output_rows_dev_by_template:
                    output_rows_dev_by_template[template_id].append(line)
                else:
                    output_rows_dev_by_template[template_id] = [line]
                output_rows_dev.append(line)
                guid_dev += 1
            else:
                output_rows_test.append([guid_test]+generated_template)
                guid_test += 1

            existing_templates.append(generated_template)

    # filter by templates partitions
    output_rows_train_it = filter_by_template_partition(train_dev_partition, output_rows_train)
    output_rows_dev_it = filter_by_template_partition(train_dev_partition, output_rows_dev)
    output_rows_test_ivit = filter_by_template_partition(train_dev_partition, output_rows_test)
    output_rows_test_ivot = filter_by_template_partition(test_partition, output_rows_test)
    write_csv(fo_train, output_rows_train_it, output_header)
    write_csv(fo_dev, output_rows_dev_it, output_header)
    write_csv(fo_test_ivit, output_rows_test_ivit, output_header)
    write_csv(fo_test_ivot, output_rows_test_ivot, output_header)

    # few sample for train and dev sets
    train_sample_sizes = [1,2,4,8,16,32,64]
    dev_sample_sizes = list(set([int(0.2*k)+1 for k in train_sample_sizes]))
    for train_size in train_sample_sizes:
        fo_train = '%strain_%d.csv' % (fo_dir, train_size)
        output_rows = []
        for k,v in output_rows_train_by_template.items():
            output_rows.extend(v[:train_size])
        output_rows = filter_by_template_partition(train_dev_partition, output_rows)
        write_csv(fo_train, output_rows, output_header)
    for dev_size in dev_sample_sizes:
        fo_dev = '%sdev_%d.csv' % (fo_dir, dev_size)
        output_rows = []
        for k,v in output_rows_dev_by_template.items():
            output_rows.extend(v[:dev_size])
        output_rows = filter_by_template_partition(train_dev_partition, output_rows)
        write_csv(fo_dev, output_rows, output_header)


def generate_data(fo_dir, templates, train_dev_partition, test_partition, output_header):
    fo_train = '%strain_160.csv' % fo_dir
    fo_dev = '%sdev_32.csv' % fo_dir
    fo_test_ivit = '%stest_ivit_300.csv' % fo_dir
    fo_test_ivot = '%stest_ivot_300.csv' % fo_dir
    fo_test_ovit = '%stest_ovit_300.csv' % fo_dir
    fo_test_ovot = '%stest_ovot_300.csv' % fo_dir
    fo_list = [fo_train, fo_dev, fo_test_ivit, fo_test_ivot, fo_test_ovit, fo_test_ovot]

    for fo in fo_list:
        if not os.path.exists(fo_dir):
            os.makedirs(fo_dir)

    # split ind and ood vocab
    ind_ood_split()

    # IND vocab
    get_ind_data(templates, train_dev_partition, test_partition, fo_dir, fo_train, fo_dev, fo_test_ivit, fo_test_ivot, output_header)

    # OOD vocab
    get_ood_data(templates, train_dev_partition, test_partition, fo_test_ovit, fo_test_ovot, output_header)


def get_subcase_templates(templates):
    # subcase_templates: <key, value> = <subcase name, list of template ids>
    subcase_templates = {}
    for t in templates:
        if t.template in subcase_templates:
            subcase_templates[t.template].append(t.id)
        else:
            subcase_templates[t.template] = [t.id]
    print(subcase_templates)
    print(len(subcase_templates.keys()))
    return subcase_templates


def get_templates_by_subcases(subcase_partition, subcase_templates):
    template_partition = []
    for subcase in subcase_partition:
        template_partition.extend(subcase_templates[subcase])
    template_partition_int = [int(item) for item in template_partition]
    return template_partition_int


def main():
    split_type = eval(sys.argv[1])
    
    global vocab_split_setting
    # = 1 if we split every type of word into ind and ood vocab
    # = 2 if we only split for N, V, Adv and Adj
    # = 3 if we split only when there are >= 4 words 
    
    # 1: V - split all; T - by templates
    if split_type == 1:
        vocab_split_setting = 1
        local_out_dir_name = 'split_all_words_templates' 
        print('Data: split_all_words_templates (split vocab on all word types ; split templates randomly).')

    # # 2: V - on certain type; T - by templates
    # elif split_type == 2:
    #     vocab_split_setting = 2
    #     local_out_dir_name = 'generated_data_new_setting'
    #     print('Data: generated_data_new_setting (split vocab only on N,V,Adv,Adj ; split templates randomly).')

    # 3: V - on >= 4; T - by templates
    elif split_type == 3:
        vocab_split_setting = 3 
        local_out_dir_name = 'split_abundant_words_templates'
        print('Data: split_abundant_words_templates (split only when there are >= 4 words ; split templates randomly).')
    # 4: V - split all; T - by subcases
    elif split_type == 4:
        vocab_split_setting = 1 
        local_out_dir_name = 'split_all_words_subcases'
        print('Data: split_all_words_subcases (split vocab on all word types ; split subcase randomly).') 
    # 5: V - on >= 4; T - by subcases
    elif split_type == 5:
        vocab_split_setting = 3 
        local_out_dir_name = 'split_abundant_words_subcases'
        print('Data: split_abundant_words_subcases (split only when there are >= 4 words ; split subcase randomly).')
    # 6: V - on certain type; T - hard split 
    elif split_type == 6:
        vocab_split_setting = 2 # maybe change if vocab_split_setting 3 works better
        local_out_dir_name = 'hard_test_templates'
        print('Data: hard_test_templates (split vocab only on N,V,Adv,Adj ; split chosen templates).')
    else:
        print('Error: invalid setting.')
        return

    fi = './templates.csv'
    # read templates 
    templates = read_templates(fi)
    template_indices = [i for i in range(118)]
    output_header = ["guid", "template_id", "heuristic", "template", "subtemplate_id", "label", "premise", "hypothesis", \
                     "high_quality", "extreme_low_quality", "var_list", \
                     "example_premise", "example_hypotheis", "example_high_quality", \
                     "example_extreme_low_quality"]

    if split_type == 1 or split_type == 2 or split_type == 3: # split T by random templates
        # introduce randomness
        num_seeds = 1
        random.seed(2021)
        seeds = random.sample(range(1, 2021), num_seeds)

        for seed_index in range(num_seeds): 
            random.seed(seeds[seed_index]) # setting the seed here works for functions imported from templates too
            random.shuffle(template_indices)

            partition1 = template_indices[0:24]
            partition2 = template_indices[24:48]
            partition3 = template_indices[48:72]
            partition4 = template_indices[72:95]
            partition5 = template_indices[95:118]

            partitions = [partition1, partition2, partition3, partition4, partition5]

            for partition_index in range(5):
                train_dev_partition, test_partition = get_train_dev_test_partitions(partitions, partition_index)

                # output file names
                fo_dir = '/net/scratch/zhouy1/%s/seed%d/partition%d/' % (local_out_dir_name, seed_index, partition_index) 

                generate_data(fo_dir, templates, train_dev_partition, test_partition, output_header)
    elif split_type == 4 or split_type == 5: # split T by random subcases
        # introduce randomness
        num_seeds = 1
        random.seed(2021)
        seeds = random.sample(range(1, 2021), num_seeds)

        for seed_index in range(num_seeds): 
            random.seed(seeds[seed_index]) # setting the seed here works for functions imported from templates too
            
            # subcase_templates: <key, value> = <subcase name, list of template ids>
            subcase_templates = get_subcase_templates(templates)
            assert len(subcase_templates)==30
            
            # test subcases (each partition): randomly sample 1 per heuristic per label
            subcase_names = list(subcase_templates.keys())
            assert len(subcase_names)==30
            random.shuffle(subcase_names)

            # subcase names partitions
            subcase_partition1 = subcase_names[0:6]
            subcase_partition2 = subcase_names[6:12]
            subcase_partition3 = subcase_names[12:18]
            subcase_partition4 = subcase_names[18:24]
            subcase_partition5 = subcase_names[24:30]

            # templates partitions
            partition1 = get_templates_by_subcases(subcase_partition1, subcase_templates)
            partition2 = get_templates_by_subcases(subcase_partition2, subcase_templates)
            partition3 = get_templates_by_subcases(subcase_partition3, subcase_templates)
            partition4 = get_templates_by_subcases(subcase_partition4, subcase_templates)
            partition5 = get_templates_by_subcases(subcase_partition5, subcase_templates)

            partitions = [partition1, partition2, partition3, partition4, partition5]

            for partition_index in range(5):
                train_dev_partition, test_partition = get_train_dev_test_partitions(partitions, partition_index)

                # output file names
                fo_dir = '../../hans-forked/auto/%s/seed%d/partition%d/' % (local_out_dir_name, seed_index, partition_index) 
                
                generate_data(fo_dir, templates, train_dev_partition, test_partition, output_header)


    elif split_type == 6:
        test_partition = [37, 38, 6, 7, 30, 31, 96, 97, 98, 99, 100, 101, 102, 103, 51, 52, 53, 1, 2, 3, 8, 9, 10, 11]
        train_dev_partition = [p for p in template_indices if p not in test_partition]
        print('test_partition: ', len(test_partition))
        print('train_dev_partition: ', len(train_dev_partition))
        fo_dir = '../../hans-forked/auto/%s/seed%d/partition%d/' % (local_out_dir_name, 0, 0) 
        generate_data(fo_dir, templates, train_dev_partition, test_partition, output_header)
    else:
        print('Error: invalid setting.')
        return


if __name__=="__main__":
    main()
