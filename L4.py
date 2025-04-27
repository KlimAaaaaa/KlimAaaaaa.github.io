# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 12:23:01 2025

@author: Анна
"""
from Bio import SeqIO

def process_genbank_file(input_file):
    # Часть 1: Сортировка по GC-составу
    print("=== Последовательности, отсортированные по GC-составу ===")
    gc_data = []
    for record in SeqIO.parse(input_file, "genbank"):
        seq = record.seq
        if len(seq) == 0:
            continue
        gc_content = (seq.count("G") + seq.count("C")) / len(seq)
        gc_data.append((gc_content, record))
    
    # Сортировка по возрастанию GC
    gc_data_sorted = sorted(gc_data, key=lambda x: x[0])
    
    # Вывод отсортированных записей
    for gc, record in gc_data_sorted:
        print(f"{record.id}: {record.description}, GC = {gc:.5f}")
    print("\n" + "="*80 + "\n")
    
    # Часть 2: Извлечение белковых последовательностей из CDS
    print("=== Белковые последовательности из CDS ===")
    for gc, record in gc_data_sorted: 
        print(f"\n{record.id}: {record.description}")
        
        for feature in record.features:
            if feature.type == "CDS":
                strand = "+" if feature.location.strand > 0 else "-"
                loc = f"[{feature.location.start}:{feature.location.end}]({strand})"
                
                # Извлекаем и транслируем последовательность
                cds_seq = feature.extract(record.seq)
                protein_seq = cds_seq.translate(table=1, to_stop=True)
                
                print(f"Coding sequence location = {loc}")
                print("Translation =")
                
                # Форматируем вывод белка (60 символов в строке)
                for i in range(0, len(protein_seq), 60):
                    print(protein_seq[i:i+60])
                print()

input_file = r"C:\sequence.gb"  
process_genbank_file(input_file)
