# -*- coding: utf-8 -*-
#
# This file is part of sensim

"""Helpers for sentence semantic similarity model.

.. Author:: Hussein AL-NATSHEH <hussein.al-natsheh@ish-lyon.cnrs.fr>

"""

from polyglot.text import Text
import spacy
import numpy as np
global parser
parser = spacy.load('en')
def get_text(s):
    return s

def get_words(s):
    text = Text(s)
    text.language = 'en'
    return text.words

def spacy_name_entities(s):
    global parser # = spacy.load('en') # This is causing a memory problem being called each time we call the function
    text = parser(unicode(s, 'utf-8'))
    entities = list(text.ents)
    org = list(' ')
    loc = list(' ')
    per = list(' ')
    norp = list(' ')
    fac = list(' ')
    gpe = list(' ')
    product = list(' ')
    event = list(' ')
    work_of_art = list(' ')
    law = list(' ')
    language = list(' ')
    for entity in entities:
        if entity.label_ == 'ORG':
            org.append(entity)
        if entity.label_ == 'PERSON':
            per.append(entity)
        if entity.label_ == 'LOC':
            loc.append(entity)
        if entity.label_ == 'NORP':
            norp.append(entity)
        if entity.label_ == 'FAC':
            fac.append(entity)
        if entity.label_ == 'GPE':
            gpe.append(entity)
        if entity.label_ == 'PRODUCT':
            product.append(entity)
        if entity.label_ == 'EVENT':
            event.append(entity)
        if entity.label_ == 'WORK_OF_ART':
            work_of_art.append(entity)
        if entity.label_ == 'LAW':
            law.append(entity)
        if entity.label_ == 'LANGUAGE':
            language.append(entity)
    return org, per, loc, norp, fac, gpe, product, event, work_of_art, law, language

def spacy_organizations(s):
    org, _, _, _, _, _, _, _, _, _, _ = spacy_name_entities(s)
    return org

def spacy_persons(s):
    _, per, _, _, _, _, _, _, _, _, _ = spacy_name_entities(s)
    return per

def spacy_locations(s):
    _, _, loc, _, _, _, _, _, _, _, _ = spacy_name_entities(s)
    return loc

def spacy_groups(s):
    _, _, _, norp, _, _, _, _, _, _, _ = spacy_name_entities(s)
    return norp

def spacy_facilities(s):
    _, _, _, _, fac, _, _, _, _, _, _ = spacy_name_entities(s)
    return fac

def spacy_geo_locations(s):
    _, _, _, _, _, gpe, _, _, _, _, _ = spacy_name_entities(s)
    return gpe

def spacy_products(s):
    _, _, _, _, _, _, product, _, _, _, _ = spacy_name_entities(s)
    return product

def spacy_events(s):
    _, _, _, _, _, _, _, event, _, _, _ = spacy_name_entities(s)
    return event

def spacy_work_of_arts(s):
    _, _, _, _, _, _, _, _, work_of_art, _, _ = spacy_name_entities(s)
    return work_of_art

def spacy_laws(s):
    _, _, _, _, _, _, _, _, _, law, _ = spacy_name_entities(s)
    return law

def spacy_languages(s):
    _, _, _, _, _, _, _, _, _, _, language = spacy_name_entities(s)
    return language

def get_name_entities(s):
    text = Text(s)
    text.language = 'en'
    entities = text.entities
    org = list(' ')
    loc = list(' ')
    per = list(' ')
    for entity in entities:
        if entity.tag == 'I-ORG':
            org = list(entity)
        elif entity.tag == 'I-PER':
            per = list(entity)
        else:
            loc = list(entity)
    return org, per, loc

def get_organizations(s):
    org, _, _ = get_name_entities(s)
    return org

def get_persons(s):
    _, per, _ = get_name_entities(s)
    return per

def get_locations(s):
    _, _, loc = get_name_entities(s)
    return loc

def get_pos(s):
    """Get dictionary of list POS_tags words from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: Dictionay
        Dictionary of list POS_tags words
    """
    def get_pos(pos, pos_codes):
        for w in text.words:
            if w.pos_tag == pos_code:
                pos.append(w)
        if len(pos) > 0:
            return pos
        else:
            return ([' '])
    text = Text(s)
    text.language = 'en'
    text.pos_tags
    POS = {}
    pos_lst = []
    adjectives = []
    pos_lst.append((adjectives, 'ADJ'))
    adpositions = []
    pos_lst.append((adpositions, 'ADP'))
    adverbs = []
    pos_lst.append((adverbs, 'ADV'))
    auxiliary_verbs = []
    pos_lst.append((auxiliary_verbs, 'AUX'))
    coordinating_conjunctions = []
    pos_lst.append((coordinating_conjunctions, 'CONJ'))
    determiners = []
    pos_lst.append((determiners, 'DET'))
    interjections = []
    pos_lst.append((interjections, 'INTJ'))
    nouns = []
    pos_lst.append((nouns, 'NOUN'))
    numerals = []
    pos_lst.append((numerals, 'NUM'))
    particles = []
    pos_lst.append((particles, 'PART'))
    pronouns = []
    pos_lst.append((pronouns, 'PRON'))
    proper_nouns = []
    pos_lst.append((proper_nouns, 'PROPN'))
    punctuations = []
    pos_lst.append((punctuations, 'PUNCT'))
    subordinating_conjunctions = []
    pos_lst.append((subordinating_conjunctions, 'SCONJ'))
    symbols = []
    pos_lst.append((symbols, 'SYM'))
    verbs = []
    pos_lst.append((verbs, 'VERB'))
    others = []
    pos_lst.append((others, 'X'))
    for pos, pos_code in pos_lst:
        POS[pos_code] = get_pos(pos, pos_code)
    return POS

def get_punctuation(s):
    """Get the punctuation from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        punctuation
    """
    punctuations = get_pos(s)['PUNCT']
    return (punctuations[0])

def get_particle(s):
    """Get the particle from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        particle
    """
    particles = get_pos(s)['PART']
    return (particles[0])

def get_determiner(s):
    """Get the determiner from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        determiner
    """
    determiners = get_pos(s)['DET']
    return (determiners[0])

def get_interjection(s):
    """Get the interjection from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        interjection
    """
    interjections = get_pos(s)['INTJ']
    return (interjections[0])

def get_coordinating_conjunction(s):
    """Get the coordinating_conjunction from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        coordinating_conjunction
    """
    coordinating_conjunctions = get_pos(s)['CONJ']
    return (coordinating_conjunctions[0])

def get_symbol(s):
    """Get the symbol from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        symbol
    """
    symbols = get_pos(s)['SYM']
    return (symbols[0])

def get_nouns(s):
    """Get list of nouns from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: list of strings
        list of nouns
    """
    return (get_pos(s)['NOUN'])

def get_1st_noun(s):
    """Get first noun from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        first noun
    """
    nouns = get_nouns(s)
    return nouns[0]

def get_2nd_noun(s):
    """Get second noun from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        second noun
    """
    nouns = get_nouns(s)
    if len(nouns) > 1:
        return nouns[1]
    else:
        return (' ')

def get_proper_nouns(s):
    """Get list of proper_nouns from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: list of strings
        list of proper_nouns
    """
    return (get_pos(s)['PROPN'])

def get_1st_proper_noun(s):
    """Get first proper_noun from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        first proper_noun
    """
    proper_nouns = get_proper_nouns(s)
    return proper_nouns[0]

def get_2nd_proper_noun(s):
    """Get second proper_noun from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        second proper_noun
    """
    proper_nouns = get_proper_nouns(s)
    if len(proper_nouns) > 1:
        return proper_nouns[1]
    else:
        return (' ')

def get_pronouns(s):
    """Get list of pronouns from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: list of strings
        list of pronouns
    """
    return (get_pos(s)['PRON'])

def get_1st_pronoun(s):
    """Get first pronoun from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        first pronoun
    """
    pronouns = get_pronouns(s)
    return pronouns[0]

def get_2nd_pronoun(s):
    """Get second pronoun from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        second pronoun
    """
    pronouns = get_pronouns(s)
    if len(pronouns) > 1:
        return pronouns[1]
    else:
        return (' ')

def get_verbs(s):
    """Get list of verbs from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: list of strings
        list of verbs
    """
    return (get_pos(s)['VERB'])

def get_1st_verb(s):
    """Get first verb from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        first verb
    """
    verbs = get_verbs(s)
    return verbs[0]

def get_2nd_verb(s):
    """Get second verb from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        second verb
    """
    verbs = get_verbs(s)
    if len(verbs) > 1:
        return verbs[1]
    else:
        return (' ')

def get_auxiliary_verbs(s):
    """Get list of auxiliary_verbs from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: list of strings
        list of auxiliary_verbs
    """
    return (get_pos(s)['AUX'])

def get_1st_auxiliary_verb(s):
    """Get first auxiliary_verb from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        first auxiliary_verb
    """
    auxiliary_verbs = get_auxiliary_verbs(s)
    return auxiliary_verbs[0]

def get_2nd_auxiliary_verb(s):
    """Get second auxiliary_verb from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        second auxiliary_verb
    """
    auxiliary_verbs = get_auxiliary_verbs(s)
    if len(auxiliary_verbs) > 1:
        return auxiliary_verbs[1]
    else:
        return (' ')

def get_adjectives(s):
    """Get list of adjectives from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: list of strings
        list of adjectives
    """
    return (get_pos(s)['ADJ'])

def get_1st_adjective(s):
    """Get first adjective from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        first adjective
    """
    adjectives = get_adjectives(s)
    return adjectives[0]

def get_2nd_adjective(s):
    """Get second adjective from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        second adjective
    """
    adjectives = get_adjectives(s)
    if len(adjectives) > 1:
        return adjectives[1]
    else:
        return (' ')

def get_adverbs(s):
    """Get list of adverbs from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: list of strings
        list of adverbs
    """
    return (get_pos(s)['ADV'])

def get_1st_adverb(s):
    """Get first adverb from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        first adverb
    """
    adverbs = get_adverbs(s)
    return adverbs[0]

def get_2nd_adverb(s):
    """Get second adverb from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        second adverb
    """
    adverbs = get_adverbs(s)
    if len(adverbs) > 1:
        return adverbs[1]
    else:
        return (' ')


def get_numbers(s):
    """Get list of numbers from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: list of strings
        list of numbers
    """
    return (get_pos(s)['NUM'])

def get_1st_number(s):
    """Get first number from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        first number
    """
    numbers = get_numbers(s)
    return numbers[0]

def get_2nd_number(s):
    """Get second number from the sentence.

    Parameters
    ----------
    :param s: string
        Sentence

    Returns
    -------
    :returns: string
        second number
    """
    numbers = get_numbers(s)
    if len(numbers) > 1:
        return numbers[1]
    else:
        return (' ')

def group_by_sentence(r):
    """Grouping function for ``PairTransformer``.

    Parameters
    ----------
    :param r: iterable
        sentence in a singleton.

    Returns
    -------
    :returns: string
        Sentence id
    """
    return r[0]["sentence_id"]
