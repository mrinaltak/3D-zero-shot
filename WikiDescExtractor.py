#!/usr/bin/env python
# coding: utf-8
# Author: Mrinal Tak
#!pip install wikipedia
import wikipedia
import spacy
nlp = spacy.load('en_core_web_sm')

with open('./data/modelnet40_normal_resampled/modelnet40_shape_names.txt') as f:
    shape_names = f.read().splitlines()
    
shape_names_wikipages = ['airplane',
                         'bathtub',
                         'bed',
                         'Bench (furniture)',
                         'bookshelf',
                         'bottle',
                         'bowl',
                         'car',
                         'chair',
                         'cone',
                         'cup',
                         'curtain',
                         'desk',
                         'door',
                         'Chest of drawers',
                         'flower_pot',
                         'glass_box',
                         'guitar',
                         'Keyboard instrument',
                         'Oil lamp',
                         'laptop',
                         'mantel',
                         'Computer monitor',
                         'night_stand',
                         'person',
                         'piano',
                         'plant',
                         'radio',
                         'range_hood',
                         'sink',
                         'sofa',
                         'stairs',
                         'Stool (seat)',
                         'Table (furniture)',
                         'tent',
                         'toilet',
                         'Entertainment center',
                         'vase',
                         'wardrobe',
                         'xbox']

wiki_desc = []
for shape_name in shape_names_wikipages:
    p = wikipedia.page(shape_name,auto_suggest=False)
    text_sentences = [sentence.text for sentence in nlp(p.content).sents][0:3]
    desc =  " ".join(text_sentences)
    wiki_desc.append(desc.replace('\n', ' '))
    
with open('wiki_desc.txt', 'w') as f:
    for item in wiki_desc:
        f.write("%s\n" % item.replace('\n', ' '))

