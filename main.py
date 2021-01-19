
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

ACTG_go!
Demonstrações Educacionais para Bioinformática
=============

Construir experiência de formação para a compreensão de alguns algoritmos de bioinformática mais usados. 
Tal formação consolida os esforços adotados pela ENAM, que por meio deste programa eleva o nível destas discussões 
com a sociedade, e correlaciona as ações de educação a distância na UnB adaptando à realidade profissional dos envolvidos, 
priorizando a interação e a troca de experiências entre magistrados, advogados e demais voluntários atuantes nesta área.

'''


from kivy.graphics import *
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.app import App
import webbrowser  # Navegador
from io import BytesIO
from data.scripts.image_editor import ed  # Módulo
import pylab
from Bio.Blast.Applications import *
from Bio.SeqUtils import GC
from Bio import SeqIO
from Bio.Seq import Seq  # Biopython
from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
from kivy.uix.image import Image
from kivy.uix.widget import Widget
import kivy
import os
import re

kivy.require('1.11.1')

# Cor de Fundo, largura e altura da janela
Window.clearcolor = get_color_from_hex('#8a3565')
Window.size = (414, 736)

# Esolher Linguagem padrão do sistema
language = 'PT-BR'

if language == 'EN':
    pass

elif language == 'PT-BR':
    # Tela do Menu
    text_programaTitle = '[color=#ffffff][size=28][b]ATCG[i]_go![/color][/i][/b][/size][/color]\n[color=#f4eef8][size=16]Demonstrações Educacionais para Bioinformática[/color][/size][/color]'
    text_programaTitle_screen = '[color=#ffffff][size=42][b]ATCG[i]_go![/color][/i][/b][/size][/color]\n[color=#f4eef8][size=20]Demonstrações Educacionais para Bioinformática[/color][/size][/color]'
    text_exitMessage = 'Deseja sair?'
    text_aboutMessage = 'Developed by:\n\n\nMr. Clenivaldo Pires da Silva\n\nDr. Julio Cesar Polonio\n\nDr. Joao Alencar Pamphile\n\n\nContact email: \n\n\nWebsite: lbiomic.uem.br'
    text_acknowledgements = 'Agradecimentos'
    text_about = 'Sobre'
    text_yes = 'Sim'
    text_no = 'Não'
    text_back = 'Voltar'
    text_next = 'Avançar'
    text_config = 'Linguagem'
    text_actionbar = 'Seja Bem-Vindo(a):'
    text_version = '[color=#ffffff][size=14][i]V. 0.1[/color][/i]'
    # ìcones do Menu
    title_image_1 = 'analizar_fasta.png'
    title_image_2 = 'alinhamento.png'
    title_image_3 = 'vacabulario.png'
    title_image_4 = 'sobre.png'
    title_image_5 = 'sair.png'
    # Tela Editor de DNA
    text_title_DNA_editor = '[color=#000000][size=22][b]Fita de DNA[/b][/size][/color]'
    text_dna_complement = '[b]Fita de DNA complementar:[/b]'
    text_dna_reserve_complement = '[b]Fita de DNA reversa complementar:[/b]'
    text_rna = '[b]RNAm:[/b]'
    text_rna_protein = '[b]Proteína:[/b]'
    text_save = 'Salvar'
    text_message_save = 'Arquivo gerado com sucesso!'
    text_message_fasta = 'Arquivo não possui a seguinte extensão: \n .fasta, .fna, .ffn, .faa ou .frn'
    text_message_fasta_1 = 'Arquivo gerado no formato FASTA'
    text_title_popup = 'Atenção!'
    text_mensage_error_codon = 'Erro em gerar Codon!'
    # Tela do Algoritmo Needleman-Wunsch
    text_title_NeedlemanWunsc = "[color=#000000][size=22][b]Algoritmo Needleman-Wunsch[/b][/size][/color]"
    text_title_SmithWaterman = "[color=#000000][size=22][b]Algoritmo Smith-Waterman[/b][/size][/color]"
    text_sequence_A = "[b]Sequência A:[/b]"
    text_sequence_B = "[b]Sequência B:[/b]"
    text_result = "[b]Resultado:[/b]"
    text_no_nucleotideo_dna = "[color=#ff0000] --> Erro, não pertence a cadeia de DNA![/color]"
    text_no_nucleotideo_rna = "[color=#ff0000] --> Erro, não pertence a cadeia de RNA![/color]"
    text_no_amino_acids = "[color=#ff0000] --> Erro, não pertence a cadeia de Aminoácido![/color]"
    text_example_dynamic_NeedlemanWunsch = "Exemplo de Matriz Dinâmica do Algoritmo Needleman-Wunsch"
    text_example_dynamic_SmithWaterman = "Exemplo de Matriz Dinâmica do Algoritmo Smith-Waterman"
    # Tela do Menu do Algoritmos
    text_name_algoritmo_1 = "Algoritmo Needleman-Wunsch"
    text_name_algoritmo_2 = "Algoritmo Smith-Waterman"
    text_name_algoritmo_3 = "Algoritmo BLAST"
    text_name_algoritmo_4 = "Programação Dinâmica"
    text_information_algoritmo_1 = 'Exemplo de alinhamento na programação dinâmica.'
    text_information_algoritmo_2 = 'Exemplo de alinhamento global e par-a-par de duas sequências.'
    text_information_algoritmo_3 = 'Exemplo de alinhamento local de duas sequências biológicas.'
    text_information_algoritmo_4 = 'Exemplo de alinhamento global e Local de duas sequencias biológicas.'
    # DNA/RNA
    text_nucleotideo_1 = 'Ademina'
    text_nucleotideo_2 = 'Citosina'
    text_nucleotideo_3 = 'Guanina'
    text_nucleotideo_4 = 'Timina'
    text_nucleotideo_5 = 'Uracila'
    text_nucleotideo_6 = 'Purina (A ou G)'
    text_nucleotideo_7 = 'Pirimidina (C, T, ou U)'
    text_nucleotideo_8 = 'C ou A'
    text_nucleotideo_9 = 'T, U, ou G'
    text_nucleotideo_10 = 'T, U, ou A'
    text_nucleotideo_11 = 'C ou G'
    text_nucleotideo_12 = 'C, T, U, ou G (exceto A)'
    text_nucleotideo_13 = 'A, T, U, ou G (exceto C)'
    text_nucleotideo_14 = 'A, T, U, ou C (exceto G)'
    text_nucleotideo_15 = 'A, C, ou G (exceto T, exceto U)'
    text_nucleotideo_16 = 'Qualquer base (A, C, G, T, ou U)'
    text_number_bases = 'Total de Números de Bases'
    # Aminoácidos
    text_amino_acids_1 = "Gly, Gli = Glicina ou Glicocola = Ácido 2-aminoacético ou Ácido 2-amino-etanóico"
    text_amino_acids_2 = "Ala = Alanina = Ácido 2-aminopropiônico ou Ácido 2-amino-propanóico"
    text_amino_acids_3 = "Leu = Leucina = Ácido 2-aminoisocapróico ou Ácido 2-amino-4-metil-pentanóico"
    text_amino_acids_4 = "Val = Valina = Ácido 2-aminovalérico ou Ácido 2-amino-3-metil-butanóico"
    text_amino_acids_5 = "Ile = Isoleucina = Ácido 2-amino-3-metil-n-valérico ou ácido 2-amino-3-metil-pentanóico"
    text_amino_acids_6 = "Pro = Prolina = Ácido pirrolidino-2-carboxílíco"
    text_amino_acids_7 = "Phe ou Fen = Fenilalanina = Ácido 2-amino-3-fenil-propiônico ou Ácido 2-amino-3-fenil-propanóico"
    text_amino_acids_8 = "Ser = Serina = Ácido 2-amino-3-hidroxi-propiônico ou Ácido 2-amino-3-hidroxi-propanóico"
    text_amino_acids_9 = "Thr, Tre = Treonina = Ácido 2-amino-3-hidroxi-n-butírico"
    text_amino_acids_10 = "Cys, Cis = Cisteina = Ácido 2-bis-(2-amino-propiônico)-3-dissulfeto ou Ácido 3-tiol-2-amino-propanóico"
    text_amino_acids_11 = "Tyr, Tir = Tirosina = Ácido 2-amino-3-(p-hidroxifenil)propiônico ou paraidroxifenilalanina"
    text_amino_acids_12 = "Asn = Asparagina = Ácido 2-aminossuccionâmico"
    text_amino_acids_13 = "Gln = Glutamina = Ácido 2-aminoglutarâmico"
    text_amino_acids_14 = "Asp = Aspartato ou Ácido aspártico = Ácido 2-aminossuccínico ou Ácido 2-amino-butanodióico"
    text_amino_acids_15 = "Glu = Glutamato ou Ácido glutâmico = Ácido 2-aminoglutárico"
    text_amino_acids_16 = "Arg = Arginina = Ácido 2-amino-4-guanidina-n-valérico"
    text_amino_acids_17 = "Lys, Lis = Lisina = Ácido 2,6-diaminocapróico ou Ácido 2, 6-diaminoexanóico"
    text_amino_acids_18 = "His = Histidina = Ácido 2-amino-3-imidazolpropiônico"
    text_amino_acids_19 = "Trp, Tri = Triptofano = Ácido 2-amino-3-indolpropiônico"
    text_amino_acids_20 = "Met = Metionina = Ácido 2-amino-3-metiltio-n-butírico"
    text_amino_acids_21 = "Stop"
    text_amino_acids_22 = "Qualquer Aminiácido"
    text_spinner_dna = 'DNA'
    text_spinner_rna = 'RNA'
    text_spinner_amino_acids = 'Aminoácidos'
    # Tela da Programação Dinâmica Aplicada a Alinhamentos de Sequências
    text_dynamicProgramming = '[color=#000000][size=22][b]Programação Dinâmica Aplicada a Alinhamentos de Sequências[/b][/size][/color]'
    text_sequence_example = 'x = TTCATA   |   y = TGCTCGTA'
    text_mismatch = 'Mismatch: -6'
    text_match = 'Match: 5'
    text_gap = 'Gap: 0'
    text_title_calc = 'Calcular'
    # Tela do BLAST
    text_blast = 'Executar BLAST'
    text_title_blast = '[color=#000000][size=22][b]BLAST[/b][/size][/color]'
    text_mensage_error = 'Campos Vazios!'
    text_spinner_blastn = 'BLASTn'
    text_spinner_blastp = 'BLASTp'
    text_spinner_blastx = 'BLASTx'
    text_spinner_tblastn = 'tBLASTn'
    text_spinner_tblastx = 'tBLASTx'


# Telas dos Programa
Builder.load_file("data/screen/kvlang.kv")


class Screen_Splash(Screen):
    '''
    Classe esponsável pelo Splash
    '''

    text_programaTitle_screen = text_programaTitle_screen

    def __init__(self, **kwargs):
        # Função Construtora
        super(Screen_Splash, self).__init__(**kwargs)
        Clock.schedule_once(self.change_screen, 5)

    def change_screen(self, name):
        # Transição de Tela
        self.manager.transition.direction = 'left'
        self.manager.duration = 1
        self.manager.current = 'menu'


class Screen_Menu(Screen):
    '''
    Classe referente a Tela do Menu, a organização do menus estão em GridLayout,
    e também possui popup de confirmação de saída e de About.

    '''

    text_programaTitle = text_programaTitle
    text_exitMessage = text_exitMessage
    text_aboutMessage = text_aboutMessage
    text_acknowledgements = text_acknowledgements
    text_config = text_config
    text_actionbar = text_actionbar
    text_version = text_version
    title_image_1 = title_image_1
    title_image_2 = title_image_2
    title_image_3 = title_image_3
    title_image_4 = title_image_4
    title_image_5 = title_image_5
    text_about = text_about
    text_yes = text_yes
    text_no = text_no

    def confirm_exit(self):
        # Função resposável em chamar popup para sair do programa
        layout = BoxLayout(orientation='vertical',
                           spacing=20, padding=[20, 20, 20, 20])
        layout_button = GridLayout(cols=2, spacing=20)
        button_yes = Button(text=text_yes, size_hint_y=None, height=48, background_color=(
            0, 1, 0, 1), background_normal=(''), background_down=(''))
        button_no = Button(text=self.text_no, size_hint_y=None, height=48, background_color=(
            1, 0, 0, 1), background_normal=(''), background_down=(''))
        image = Image(source='data/icons/atencion.png')
        layout.add_widget(image)
        layout_button.add_widget(button_yes)
        layout_button.add_widget(button_no)
        layout.add_widget(layout_button)
        popup = Popup(title=text_exitMessage, content=layout, size_hint=(None, None), size=(
            100, 100), background='atlas://data/images/defaulttheme/button_pressed')
        button_yes.bind(on_press=App.get_running_app().stop)
        button_no.bind(on_press=popup.dismiss)
        animText = Animation(color=(0, 0, 0, 1)) + \
            Animation(color=(1, 1, 1, 1))
        animText.repeat = True
        animText.start(button_yes)
        animation = Animation(size=(300, 250), duration=0.3, t='out_back')
        animation.start(popup)
        popup.open()

    def about(self):
        # Função resposável em chamar popup para mostrar autores e as lincenças
        layout = BoxLayout(orientation='vertical',
                           spacing=20, padding=[20, 20, 20, 20])
        label = Label(text=text_aboutMessage, halign='left', markup=True)
        button_acknowledgements = Button(text=text_acknowledgements, size_hint_y=None, height=48, background_color=(
            1, 0, 0, 1), background_normal=(''), background_down=(''))
        button_close = Button(text='OK', size_hint_y=None, height=48, background_color=(
            1, 0, 0, 1), background_normal=(''), background_down=(''))
        layout.add_widget(label)
        layout.add_widget(button_acknowledgements)
        layout.add_widget(button_close)
        popup = Popup(title=text_about, content=layout, size_hint=(None, None), size=(
            100, 100), background='atlas://data/images/defaulttheme/button_pressed')
        button_close.bind(on_press=popup.dismiss)
        animation = Animation(size=(300, 550), duration=0.3, t='out_back')
        animation.start(popup)
        popup.open()


class Screen_1(Screen):
    '''
    Classe responsavel pelo tela carregamento de informações da cadeia de DNA
    '''

    text_title_DNA_editor = text_title_DNA_editor
    text_no_nucleotideo_dna = text_no_nucleotideo_dna
    text_nucleotideo_1 = text_nucleotideo_1  # DNA
    text_nucleotideo_2 = text_nucleotideo_2
    text_nucleotideo_3 = text_nucleotideo_3
    text_nucleotideo_4 = text_nucleotideo_4
    text_nucleotideo_6 = text_nucleotideo_6
    text_nucleotideo_7 = text_nucleotideo_7
    text_nucleotideo_8 = text_nucleotideo_8
    text_nucleotideo_9 = text_nucleotideo_9
    text_nucleotideo_10 = text_nucleotideo_10
    text_nucleotideo_11 = text_nucleotideo_11
    text_nucleotideo_12 = text_nucleotideo_12
    text_nucleotideo_13 = text_nucleotideo_13
    text_nucleotideo_14 = text_nucleotideo_14
    text_nucleotideo_15 = text_nucleotideo_15
    text_nucleotideo_16 = text_nucleotideo_16
    text_amino_acids_1 = text_amino_acids_1  # Aminoácidos
    text_amino_acids_2 = text_amino_acids_2
    text_amino_acids_3 = text_amino_acids_3
    text_amino_acids_4 = text_amino_acids_4
    text_amino_acids_5 = text_amino_acids_5
    text_amino_acids_6 = text_amino_acids_6
    text_amino_acids_7 = text_amino_acids_7
    text_amino_acids_8 = text_amino_acids_8
    text_amino_acids_9 = text_amino_acids_9
    text_amino_acids_10 = text_amino_acids_10
    text_amino_acids_11 = text_amino_acids_11
    text_amino_acids_12 = text_amino_acids_12
    text_amino_acids_13 = text_amino_acids_13
    text_amino_acids_14 = text_amino_acids_14
    text_amino_acids_15 = text_amino_acids_15
    text_amino_acids_16 = text_amino_acids_16
    text_amino_acids_17 = text_amino_acids_17
    text_amino_acids_18 = text_amino_acids_18
    text_amino_acids_19 = text_amino_acids_19
    text_amino_acids_20 = text_amino_acids_20
    text_amino_acids_21 = text_amino_acids_21
    text_amino_acids_22 = text_amino_acids_22
    text_number_bases = text_number_bases
    text_blast = text_blast
    text_dna_complement = text_dna_complement
    text_dna_reserve_complement = text_dna_reserve_complement
    text_rna = text_rna
    text_rna_protein = text_rna_protein
    text_save = text_save
    text_back = text_back
    text_message_save = text_message_save
    text_message_fasta = text_message_fasta
    text_title_popup = text_title_popup
    text_mensage_error_codon = text_mensage_error_codon

    def __init__(self, **kwargs):
        # Função Construtora
        super(Screen_1, self).__init__(**kwargs)
        Clock.schedule_once(self.activate_graphic, 1)
        Window.bind(on_dropfile=self.let_go)

    def let_go(self, window, way):
        way = way.decode("utf-8")
        name, extension = os.path.splitext(way)

        # Verificar se arquivo é padrão utilizado da Bioinformática
        if extension == '.fasta' or extension == '.fna' or extension == '.ffn' or extension == '.faa' or extension == '.frn':
            fasta = way
            relist = []

            # Remover primeira linha ">"
            file = open(fasta, 'r')
            fist_line = file.readline()  # Primeira Linha
            for line in file:
                if line.find('>') != 0:
                    relist.append(line)

            # Remover caracteres [] '' \n ,
            fist_line = fist_line.replace('>', '')
            fist_line = fist_line.replace('\\n', '')
            seq = str(relist)[1:-1]
            seq = seq.replace("'", "")
            seq = seq.replace('\\n', '')
            seq = seq.replace(',', '')

            # Remover espaço entre as letras
            pattern = re.compile(r'\s+')
            seq = re.sub(pattern, '', seq)

            # Contar o número de nucleotídeos presentes na cadeia
            a = 0  # Adenina
            t = 0  # Timina
            g = 0  # Guanina
            c = 0  # Citosina
            x = 0  # Qualquer nucleotídeo
            e = 0  # Erro

            # Verificar os nucleotídeos digitados pertecem a cadeia de DNA
            for n in seq:
                if n == 'A' or n == 'a':
                    a = a + 1
                elif n == 'C' or n == 'c':
                    t = t + 1
                elif n == 'G' or n == 'g':
                    g = g + 1
                elif n == 'T' or n == 't':
                    c = c + 1
                    x = x + 1
                elif n == 'R' or n == 'r':
                    x = x + 1
                elif n == 'Y' or n == 'y':
                    x = x + 1
                elif n == 'M' or n == 'm':
                    x = x + 1
                elif n == 'K' or n == 'k':
                    x = x + 1
                elif n == 'W' or n == 'w':
                    x = x + 1
                elif n == 'S' or n == 's':
                    x = x + 1
                elif n == 'B' or n == 'b':
                    x = x + 1
                elif n == 'D' or n == 'd':
                    x = x + 1
                elif n == 'H' or n == 'h':
                    x = x + 1
                elif n == 'V' or n == 'v':
                    x = x + 1
                elif n == 'N' or n == 'n':
                    x = x + 1
                else:
                    e = e + 1

            # Soma
            s = a + t + g + c + x

            # DNA -> Transcrição -> Tradução
            dna = Seq(seq)
            dna_complement = str(dna.complement())
            dna_reverse_complement = str(dna.reverse_complement())
            rna = str(dna.transcribe())
            rna_protein = str(dna.translate())

            gc = GC(dna)
            at = 100 - gc

            # Gravar informações geradas a partir do arquivo .fasta
            file = open('data/tmp/sequence.fasta', 'w')
            file.writelines(fist_line + '\n')
            file.writelines(text_nucleotideo_1 + ': ' + str(a) + '\n' + text_nucleotideo_2 + ': ' + str(t) + '\n' + text_nucleotideo_3 +
                            ': ' + str(g) + '\n' + text_nucleotideo_4 + ': ' + str(c) + '\n' + text_number_bases + ': ' +
                            str(s) + '\nError: ' + str(e) + '\n' + 'GC: %0.1f | AT: %0.1f' % (gc, at) + '\n\n')
            file.writelines('> ' + 'DNA' + '\n' + str(dna) + '\n\n')
            file.writelines('> ' + 'DNA Complement' + '\n' +
                            str(dna_complement) + '\n\n')
            file.writelines('> ' + 'DNA Reverse Complement' + '\n' +
                            str(dna_reverse_complement) + '\n\n')
            file.writelines('> ' + 'RNA' + '\n' + str(rna) + '\n\n')
            file.writelines('> ' + 'Amino Acids' + '\n' +
                            str(rna_protein) + '\n\n')
            file.writelines('Extended Name of Amino Acids:' + '\n\n')

            # Nome dos Aminoácidos
            for n in rna_protein:
                if n == 'G':
                    file.writelines(n + ' = ' + text_amino_acids_1 + '\n')
                elif n == 'A':
                    file.writelines(n + ' = ' + text_amino_acids_2 + '\n')
                elif n == 'L':
                    file.writelines(n + ' = ' + text_amino_acids_3 + '\n')
                elif n == 'V':
                    file.writelines(n + ' = ' + text_amino_acids_4 + '\n')
                elif n == 'I':
                    file.writelines(n + ' = ' + text_amino_acids_5 + '\n')
                elif n == 'P':
                    file.writelines(n + ' = ' + text_amino_acids_6 + '\n')
                elif n == 'F':
                    file.writelines(n + ' = ' + text_amino_acids_7 + '\n')
                elif n == 'S':
                    file.writelines(n + ' = ' + text_amino_acids_8 + '\n')
                elif n == 'T':
                    file.writelines(n + ' = ' + text_amino_acids_9 + '\n')
                elif n == 'C':
                    file.writelines(n + ' = ' + text_amino_acids_10 + '\n')
                elif n == 'Y':
                    file.writelines(n + ' = ' + text_amino_acids_11 + '\n')
                elif n == 'N':
                    file.writelines(n + ' = ' + text_amino_acids_12 + '\n')
                elif n == 'Q':
                    file.writelines(n + ' = ' + text_amino_acids_13 + '\n')
                elif n == 'D':
                    file.writelines(n + ' = ' + text_amino_acids_14 + '\n')
                elif n == 'E':
                    file.writelines(n + ' = ' + text_amino_acids_15 + '\n')
                elif n == 'R':
                    file.writelines(n + ' = ' + text_amino_acids_16 + '\n')
                elif n == 'K':
                    file.writelines(n + ' = ' + text_amino_acids_17 + '\n')
                elif n == 'H':
                    file.writelines(n + ' = ' + text_amino_acids_18 + '\n')
                elif n == 'W':
                    file.writelines(n + ' = ' + text_amino_acids_19 + '\n')
                elif n == 'M':
                    file.writelines(n + ' = ' + text_amino_acids_20 + '\n')
                elif n == '*':
                    file.writelines(n + ' = ' + text_amino_acids_21 + '\n')
                elif n == 'X':
                    file.writelines(n + ' = ' + text_amino_acids_22)

            # Fechando o Arquivo
            file.close()

            # Exibir o resultado na Tela
            webbrowser.open('data/tmp/sequence.fasta', new=0, autoraise=True)

        elif extension == '.gb':
            genbank = way

            # Manipulando arquivos no formato genbank
            genomes = SeqIO.parse(genbank, 'genbank')

            # Convertendo no formato FASTA
            for genome in genomes:
                SeqIO.write(genome, genome.id + '.fasta', 'fasta')

            # Popup
            layout = BoxLayout(orientation='vertical',
                               spacing=20, padding=[20, 20, 20, 20])
            label = Label(text=text_message_fasta_1,
                          halign='left', markup=True)
            button_close = Button(text='OK', size_hint_y=None, height=48, background_color=(
                1, 0, 0, 1), background_normal=(''), background_down=(''))
            layout.add_widget(label)
            layout.add_widget(button_close)
            popup = Popup(title=text_title_popup, content=layout, size_hint=(None, None), size=(
                100, 100), background='atlas://data/images/defaulttheme/button_pressed')
            button_close.bind(on_press=popup.dismiss)
            animation = Animation(size=(300, 250), duration=0.3, t='out_back')
            animation.start(popup)
            popup.open()

        else:
            # Popup
            layout = BoxLayout(orientation='vertical',
                               spacing=20, padding=[20, 20, 20, 20])
            label = Label(text=text_message_fasta,
                          halign='left', markup=True)
            button_close = Button(text='OK', size_hint_y=None, height=48, background_color=(
                1, 0, 0, 1), background_normal=(''), background_down=(''))
            layout.add_widget(label)
            layout.add_widget(button_close)
            popup = Popup(title=text_title_popup, content=layout, size_hint=(None, None), size=(
                100, 100), background='atlas://data/images/defaulttheme/button_pressed')
            button_close.bind(on_press=popup.dismiss)
            animation = Animation(size=(300, 250), duration=0.3, t='out_back')
            animation.start(popup)
            popup.open()

    def keyboard_textInput(self):
        seq = self.ids.input_dna_editor.text

        # Contar o número de nucleotídeos presentes na cadeia
        a = 0  # Adenina
        t = 0  # Timina
        g = 0  # Guanina
        c = 0  # Citosina
        x = 0  # Qualquer nucleotídeo
        e = 0  # Erro

        # Cabeçalho
        print()
        print(30*'=-=')
        print()
        print('Aminoácidos:')
        print()

        # Verificar os nucleotídeos digitados pertecem a cadeia de DNA
        for n in seq:
            if n == 'A' or n == 'a':
                a = a + 1
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_1
            elif n == 'C' or n == 'c':
                t = t + 1
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_2
            elif n == 'G' or n == 'g':
                g = g + 1
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_3
            elif n == 'T' or n == 't':
                c = c + 1
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_4
                x = x + 1
            elif n == 'R' or n == 'r':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_6
                x = x + 1
            elif n == 'Y' or n == 'y':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_7
                x = x + 1
            elif n == 'M' or n == 'm':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_8
                x = x + 1
            elif n == 'K' or n == 'k':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_9
                x = x + 1
            elif n == 'W' or n == 'w':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_10
                x = x + 1
            elif n == 'S' or n == 's':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_11
                x = x + 1
            elif n == 'B' or n == 'b':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_12
                x = x + 1
            elif n == 'D' or n == 'd':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_13
                x = x + 1
            elif n == 'H' or n == 'h':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_14
                x = x + 1
            elif n == 'V' or n == 'v':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_15
                x = x + 1
            elif n == 'N' or n == 'n':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_16
                x = x + 1
            else:
                self.ids.no_nucleotideo.text = '[color=#ff0000]' + \
                    n + '[/color]' + text_no_nucleotideo_dna
                e = e + 1

        try:
            # DNA -> Transcrição -> Tradução
            dna = Seq(seq)
            dna_complement = str(dna.complement())
            dna_reverse_complement = str(dna.reverse_complement())
            rna = str(dna.transcribe())
            rna_protein = str(dna.translate())

            # Exibir a contagem de Nucleotídeos
            self.ids.result_id.text = text_dna_complement + ' ' + dna_complement + '\n\n' + text_dna_reserve_complement + ' ' + \
                dna_reverse_complement + '\n\n' + text_rna + ' ' + rna + \
                '\n\n' + text_rna_protein + ' ' + rna_protein

            # Exibir o Nome do Aminoácidos
            for n in rna_protein:
                if n == 'G':
                    print(n + ' = ' + text_amino_acids_1)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_1
                elif n == 'A':
                    print(n + ' = ' + text_amino_acids_2)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_2
                elif n == 'L':
                    print(n + ' = ' + text_amino_acids_3)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_3
                elif n == 'V':
                    print(n + ' = ' + text_amino_acids_4)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_4
                elif n == 'I':
                    print(n + ' = ' + text_amino_acids_5)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_5
                elif n == 'P':
                    print(n + ' = ' + text_amino_acids_6)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_6
                elif n == 'F':
                    print(n + ' = ' + text_amino_acids_7)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_7
                elif n == 'S':
                    print(n + ' = ' + text_amino_acids_8)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_8
                elif n == 'T':
                    print(n + ' = ' + text_amino_acids_9)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_9
                elif n == 'C':
                    print(n + ' = ' + text_amino_acids_10)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_10
                elif n == 'Y':
                    print(n + ' = ' + text_amino_acids_11)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_11
                elif n == 'N':
                    print(n + ' = ' + text_amino_acids_12)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_12
                elif n == 'Q':
                    print(n + ' = ' + text_amino_acids_13)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_13
                elif n == 'D':
                    print(n + ' = ' + text_amino_acids_14)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_14
                elif n == 'E':
                    print(n + ' = ' + text_amino_acids_15)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_15
                elif n == 'R':
                    print(n + ' = ' + text_amino_acids_16)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_16
                elif n == 'K':
                    print(n + ' = ' + text_amino_acids_17)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_17
                elif n == 'H':
                    print(n + ' = ' + text_amino_acids_18)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_18
                elif n == 'W':
                    print(n + ' = ' + text_amino_acids_19)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_19
                elif n == 'M':
                    print(n + ' = ' + text_amino_acids_20)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_20
                elif n == '*':
                    print(n + ' = ' + text_amino_acids_21)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_21
                elif n == 'X':
                    print(n + ' = ' + text_amino_acids_22)
                    self.ids.name_amino_acids.text = n + ' = ' + text_amino_acids_22
        except:
            self.ids.name_amino_acids.text = text_mensage_error_codon

        # Soma
        s = a + t + g + c + x

        self.ids.information_dna.text = '[b]' + text_nucleotideo_1 + '[/b]: ' + str(a) + '  |  [b]' + text_nucleotideo_2 + '[/b]: ' + str(t) + '  |  [b]' + \
            text_nucleotideo_3 + '[/b]: ' + str(g) + ' |  [b]' + text_nucleotideo_4 + \
            '[/b]: ' + str(c) + '  [b]' + '\n' + \
            text_number_bases + '[/b]: ' + \
            str(s) + ' |  [b]Error:[/b] ' + str(e)

        print()
        print(30*'=-=')
        print()

    def activate_graphic(self, name):
        Screen_1.button_graphic_gc(self)

    def button_graphic_gc(self):
        seq = self.ids.input_dna_editor.text
        dna = Seq(seq)

        # Gerar Gráfico
        gc = GC(dna)
        at = 100 - gc

        pylab.pie([gc, at])
        pylab.xlabel('GC: %0.1f\nAT: %0.1f' % (gc, at))
        pylab.savefig('data/tmp/graphic.png', format='png')  # Salva o gráfico

        # Caminho da imagem do gráfico
        way = 'data/tmp/graphic.png'
        ed.upload_image(way)

        # Carregar imagem do gráfico
        image_area = self.ids.image_area
        image_area.clear_widgets()
        img_buffer = BytesIO()
        ed.image.save(img_buffer, format=ed.image_format)
        img_buffer.seek(0)
        im = CoreImage(img_buffer, ext=ed.image_format.lower())
        texture = im.texture
        image = Image()
        image.texture = texture
        img_buffer.close()
        image_area.add_widget(image)

    def button_save_fasta(self):
        seq = self.ids.input_dna_editor.text
        dna = Seq(seq)
        dna_complement = str(dna.complement())
        dna_reverse_complement = str(dna.reverse_complement())
        rna = str(dna.transcribe())
        rna_protein = str(dna.translate())

        # Gravar as sequências em fasta
        file = open('sequence.fasta', 'w')
        file.writelines('> ' + 'DNA' + '\n' + str(dna) + '\n\n')
        file.writelines('> ' + 'DNA Complement' + '\n' +
                        str(dna_complement) + '\n\n')
        file.writelines('> ' + 'DNA Reverse Complement' + '\n' +
                        str(dna_reverse_complement) + '\n\n')
        file.writelines('> ' + 'RNA' + '\n' + str(rna) + '\n\n')
        file.writelines('> ' + 'Amino Acids' + '\n' + str(rna_protein))
        file.close()

        # Popup
        layout = BoxLayout(orientation='vertical',
                           spacing=20, padding=[20, 20, 20, 20])
        label = Label(text=text_message_save, halign='left', markup=True)
        button_close = Button(text='OK', size_hint_y=None, height=48, background_color=(
            1, 0, 0, 1), background_normal=(''), background_down=(''))
        layout.add_widget(label)
        layout.add_widget(button_close)
        popup = Popup(title=text_title_popup, content=layout, size_hint=(None, None), size=(
            100, 100), background='atlas://data/images/defaulttheme/button_pressed')
        button_close.bind(on_press=popup.dismiss)
        animation = Animation(size=(300, 250), duration=0.3, t='out_back')
        animation.start(popup)
        popup.open()

    def button_example_code(self):
        way = 'data/content/dogma_central_biologia.png'
        Screen_1.transition_screen(self, way, 'screen_1_1')

    def change_screen(self, name_screen, t="Slide", d="down"):
        if t == 'Slide':
            self.manager.transition = SlideTransition()
        else:
            self.manager.transition = NoTransition()

        # Transição de Tela
        self.manager.transition.direction = d
        self.manager.duration = 1
        self.manager.current = name_screen

    def transition_screen(self, way_image, name_screen):
        way = way_image
        name = name_screen
        if ed.upload_image(way) == False:
            pass
        else:
            screen_1_1 = self.manager.get_screen(name)
            screen_1_1.display_image()
            self.change_screen(name)


class Screen_1_1(Screen):
    '''
    Classe responsável em exibir imagem de exemplicação do dogma da biologia molecular
    '''

    text_back = text_back

    # Abir  o código de examplo do código em BioPython do Dogma Central da Biologia
    text = ''
    with open('data/content/example_code_centralDogmaBiology.txt') as code:
        for line in code:
            text += line

    def display_image(self):
        # Função responsável em adcionar imagem do gráfico na Tela do Programa
        image_area = self.ids.image_area
        image_area.clear_widgets()
        img_buffer = BytesIO()
        ed.image.save(img_buffer, format=ed.image_format)
        img_buffer.seek(0)
        im = CoreImage(img_buffer, ext=ed.image_format.lower())
        texture = im.texture
        image = Image()
        image.texture = texture
        img_buffer.close()
        image_area.add_widget(image)


class Screen_2(Screen):
    '''
    Classe responsável pelo menu dos Algoratimos de alinhamentos
    '''

    text_name_algoritmo_1 = text_name_algoritmo_1
    text_name_algoritmo_2 = text_name_algoritmo_2
    text_name_algoritmo_3 = text_name_algoritmo_3
    text_name_algoritmo_4 = text_name_algoritmo_4
    text_information_algoritmo_1 = text_information_algoritmo_1
    text_information_algoritmo_2 = text_information_algoritmo_2
    text_information_algoritmo_3 = text_information_algoritmo_3
    text_information_algoritmo_4 = text_information_algoritmo_4
    text_back = text_back

    def __init__(self, **kwargs):
        # Função Construtor
        super(Screen_2, self).__init__(**kwargs)
        self.ids.text_information_algoritmo_1.text = text_information_algoritmo_1
        self.ids.text_information_algoritmo_2.text = text_information_algoritmo_2
        self.ids.text_information_algoritmo_3.text = text_information_algoritmo_3
        self.ids.text_information_algoritmo_4.text = text_information_algoritmo_4


class Screen_2_1(Screen):
    '''
    Classe responsável por exemplificar o alinhamento de sequências por Programação Dinâmica

    '''

    text_back = text_back
    text_dynamicProgramming = text_dynamicProgramming
    text_sequence_example = text_sequence_example
    text_mismatch = text_mismatch
    text_match = text_match
    text_gap = text_gap

    def get_score1(self):
        v = str(self.ids.input_value1.text)

        # Verificar o Valor
        if v == '0':
            self.ids.input_value1.background_color = 0, 1, 0, .5
        else:
            self.ids.input_value1.background_color = 1, 0, 0, .5

    def get_score2(self):
        v = str(self.ids.input_value2.text)

        # Verificar o Valor
        if v == '-6_':
            self.ids.input_value2.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value2.background_color = 1, 0, 0, .5

    def get_score3(self):
        v = str(self.ids.input_value3.text)

        # Verificar o Valor
        if v == '-12_':
            self.ids.input_value3.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value3.background_color = 1, 0, 0, .5

    def get_score4(self):
        v = str(self.ids.input_value4.text)

        # Verificar o Valor
        if v == '-18_':
            self.ids.input_value4.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value4.background_color = 1, 0, 0, .5

    def get_score5(self):
        v = str(self.ids.input_value5.text)

        # Verificar o Valor
        if v == '-24_':
            self.ids.input_value5.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value5.background_color = 1, 0, 0, .5

    def get_score6(self):
        v = str(self.ids.input_value6.text)

        # Verificar o Valor
        if v == '-30_':
            self.ids.input_value6.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value6.background_color = 1, 0, 0, .5

    def get_score7(self):
        v = str(self.ids.input_value7.text)

        # Verificar o Valor
        if v == '-36_':
            self.ids.input_value7.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value7.background_color = 1, 0, 0, .5

    def get_score8(self):
        v = str(self.ids.input_value8.text)

        # Verificar o Valor
        if v == '-42_':
            self.ids.input_value8.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value8.background_color = 1, 0, 0, .5

    def get_score9(self):
        v = str(self.ids.input_value9.text)

        # Verificar o Valor
        if v == '-48_':
            self.ids.input_value9.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value9.background_color = 1, 0, 0, .5

    def get_score10(self):
        v = str(self.ids.input_value10.text)

        # Verificar o Valor
        if v == '-6|':
            self.ids.input_value10.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value10.background_color = 1, 0, 0, .5

    def get_score11(self):
        v = str(self.ids.input_value11.text)
        v1 = str(self.ids.input_value2.text)
        v2 = str(self.ids.input_value10.text)
        v3 = str(self.ids.input_value1.text)

        # Verificar o Valor
        if v == '5\\' and v1 == '-6_' and v2 == '-6|' and v3 == '0':
            self.ids.input_value11.background_color = 0, 5, 0, .5
            self.ids.result_id1.text = '  T'
            self.ids.result_id9.text = '  T'
            self.ids.result_id17.text = '+5'
        else:
            self.ids.input_value11.background_color = 1, 0, 0, .5

    def get_score12(self):
        v = str(self.ids.input_value12.text)
        v1 = str(self.ids.input_value3.text)
        v2 = str(self.ids.input_value11.text)
        v3 = str(self.ids.input_value2.text)

        # Verificar o Valor
        if v == '-1_' and v1 == '-12_' and v2 == '5\\' and v3 == '-6_':
            self.ids.input_value12.background_color = 0, 5, 0, .5
            self.ids.result_id2.text = '  _'
            self.ids.result_id10.text = '  G'
            self.ids.result_id18.text = ' -6'
        else:
            self.ids.input_value12.background_color = 1, 0, 0, .5

    def get_score13(self):
        v = str(self.ids.input_value13.text)
        v1 = str(self.ids.input_value4.text)
        v2 = str(self.ids.input_value12.text)
        v3 = str(self.ids.input_value3.text)

        # Verificar o Valor
        if v == '-7_' and v1 == '-18_' and v2 == '-1_' and v3 == '-12_':
            self.ids.input_value13.background_color = 0, 5, 0, .5
            self.ids.result_id3.text = '  _'
            self.ids.result_id11.text = '  C'
            self.ids.result_id19.text = '+5'
        else:
            self.ids.input_value13.background_color = 1, 0, 0, .5

    def get_score14(self):
        v = str(self.ids.input_value14.text)

        # Verificar o Valor
        if v == '-13\\_' or v == '-13_\\':
            self.ids.input_value14.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value14.background_color = 1, 0, 0, .5

    def get_score15(self):
        v = str(self.ids.input_value15.text)

        # Verificar o Valor
        if v == '-19_':
            self.ids.input_value15.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value15.background_color = 1, 0, 0, .5

    def get_score16(self):
        v = str(self.ids.input_value16.text)

        # Verificar o Valor
        if v == '-25_':
            self.ids.input_value16.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value16.background_color = 1, 0, 0, .5

    def get_score17(self):
        v = str(self.ids.input_value17.text)

        # Verificar o Valor
        if v == '-31\\_' or v == '-31_\\':
            self.ids.input_value17.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value17.background_color = 1, 0, 0, .5

    def get_score18(self):
        v = str(self.ids.input_value18.text)

        # Verificar o Valor
        if v == '-37_':
            self.ids.input_value18.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value18.background_color = 1, 0, 0, .5

    def get_score19(self):
        v = str(self.ids.input_value19.text)

        # Verificar o Valor
        if v == '-12|':
            self.ids.input_value19.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value19.background_color = 1, 0, 0, .5

    def get_score20(self):
        v = str(self.ids.input_value20.text)

        # Verificar o Valor
        if v == '-1\\|' or v == '-1|\\':
            self.ids.input_value20.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value20.background_color = 1, 0, 0, .5

    def get_score21(self):
        v = str(self.ids.input_value21.text)

        # Verificar o Valor
        if v == '3\\':
            self.ids.input_value21.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value21.background_color = 1, 0, 0, .5

    def get_score22(self):
        v = str(self.ids.input_value22.text)

        # Verificar o Valor
        if v == '-3\\_' or v == '-3_\\':
            self.ids.input_value22.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value22.background_color = 1, 0, 0, .5

    def get_score23(self):
        v = str(self.ids.input_value23.text)
        v1 = str(self.ids.input_value14.text)
        v2 = str(self.ids.input_value22.text)
        v3 = str(self.ids.input_value13.text)

        # Verificar o Valor
        if v == '-2\\' and v1 == '-13\\_' or v1 == '-13_\\' and v2 == '-3\\_' or v2 == '-3_\\' and v3 == '-7_':
            self.ids.input_value23.background_color = 0, 5, 0, .5
            self.ids.result_id4.text = '  T'
            self.ids.result_id12.text = '  T'
            self.ids.result_id20.text = '+5'
        else:
            self.ids.input_value23.background_color = 1, 0, 0, .5

    def get_score24(self):
        v = str(self.ids.input_value24.text)

        # Verificar o Valor
        if v == '-8_':
            self.ids.input_value24.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value24.background_color = 1, 0, 0, .5

    def get_score25(self):
        v = str(self.ids.input_value25.text)

        # Verificar o Valor
        if v == '-14_':
            self.ids.input_value25.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value25.background_color = 1, 0, 0, .5

    def get_score26(self):
        v = str(self.ids.input_value26.text)

        # Verificar o Valor
        if v == '-20\\_':
            self.ids.input_value26.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value26.background_color = 1, 0, 0, .5

    def get_score27(self):
        v = str(self.ids.input_value27.text)

        # Verificar o Valor
        if v == '-26_':
            self.ids.input_value27.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value27.background_color = 1, 0, 0, .5

    def get_score28(self):
        v = str(self.ids.input_value28.text)

        # Verificar o Valor
        if v == '-18|':
            self.ids.input_value28.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value28.background_color = 1, 0, 0, .5

    def get_score29(self):
        v = str(self.ids.input_value29.text)

        # Verificar o Valor
        if v == '-7|':
            self.ids.input_value29.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value29.background_color = 1, 0, 0, .5

    def get_score30(self):
        v = str(self.ids.input_value30.text)

        # Verificar o Valor
        if v == '-3\\|' or v == '-3|\\':
            self.ids.input_value30.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value30.background_color = 1, 0, 0, .5

    def get_score31(self):
        v = str(self.ids.input_value31.text)

        # Verificar o Valor
        if v == '8\\':
            self.ids.input_value31.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value31.background_color = 1, 0, 0, .5

    def get_score32(self):
        v = str(self.ids.input_value32.text)

        # Verificar o Valor
        if v == '2_':
            self.ids.input_value32.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value32.background_color = 1, 0, 0, .5

    def get_score33(self):
        v = str(self.ids.input_value33.text)
        v1 = str(self.ids.input_value32.text)
        v2 = str(self.ids.input_value24.text)
        v3 = str(self.ids.input_value23.text)

        # Verificar o Valor
        if v == '3\\' and v1 == '2_' and v2 == '-8_' and v3 == '-2\\':
            self.ids.input_value33.background_color = 0, 5, 0, .5
            self.ids.result_id5.text = '  C'
            self.ids.result_id13.text = '  C'
            self.ids.result_id21.text = '+5'
        else:
            self.ids.input_value33.background_color = 1, 0, 0, .5

    def get_score34(self):
        v = str(self.ids.input_value34.text)

        # Verificar o Valor
        if v == '-3_':
            self.ids.input_value34.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value34.background_color = 1, 0, 0, .5

    def get_score35(self):
        v = str(self.ids.input_value35.text)

        # Verificar o Valor
        if v == '-9_':
            self.ids.input_value35.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value35.background_color = 1, 0, 0, .5

    def get_score36(self):
        v = str(self.ids.input_value36.text)

        # Verificar o Valor
        if v == '-15_':
            self.ids.input_value36.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value36.background_color = 1, 0, 0, .5

    def get_score37(self):
        v = str(self.ids.input_value37.text)

        # Verificar o Valor
        if v == '-24|':
            self.ids.input_value37.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value37.background_color = 1, 0, 0, .5

    def get_score38(self):
        v = str(self.ids.input_value38.text)

        # Verificar o Valor
        if v == '-13|':
            self.ids.input_value38.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value38.background_color = 1, 0, 0, .5

    def get_score39(self):
        v = str(self.ids.input_value39.text)

        # Verificar o Valor
        if v == '-9\\|' or v == '-9|\\':
            self.ids.input_value39.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value39.background_color = 1, 0, 0, .5

    def get_score40(self):
        v = str(self.ids.input_value40.text)

        # Verificar o Valor
        if v == '2|':
            self.ids.input_value40.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value40.background_color = 1, 0, 0, .5

    def get_score41(self):
        v = str(self.ids.input_value41.text)

        # Verificar o Valor
        if v == '6\\':
            self.ids.input_value41.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value41.background_color = 1, 0, 0, .5

    def get_score42(self):
        v = str(self.ids.input_value42.text)

        # Verificar o Valor
        if v == '0\\_' or v == '0_\\':
            self.ids.input_value42.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value42.background_color = 1, 0, 0, .5

    def get_score43(self):
        v = str(self.ids.input_value43.text)
        v1 = str(self.ids.input_value33.text)
        v2 = str(self.ids.input_value34.text)
        v3 = str(self.ids.input_value42.text)

        # Verificar o Valor
        if v == '1\\' and v1 == '3\\' and v2 == '-3_' and v3 == '0\\_' or v3 == '0_\\':
            self.ids.input_value43.background_color = 0, 5, 0, .5
            self.ids.result_id6.text = '  A'
            self.ids.result_id14.text = '  G'
            self.ids.result_id22.text = ' -2'
        else:
            self.ids.input_value43.background_color = 1, 0, 0, .5

    def get_score44(self):
        v = str(self.ids.input_value44.text)

        # Verificar o Valor
        if v == '-5\\_' or v == '-5_\\':
            self.ids.input_value44.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value44.background_color = 1, 0, 0, .5

    def get_score45(self):
        v = str(self.ids.input_value45.text)

        # Verificar o Valor
        if v == '-4\\':
            self.ids.input_value45.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value45.background_color = 1, 0, 0, .5

    def get_score46(self):
        v = str(self.ids.input_value46.text)

        # Verificar o Valor
        if v == '-30|':
            self.ids.input_value46.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value46.background_color = 1, 0, 0, .5

    def get_score47(self):
        v = str(self.ids.input_value47.text)

        # Verificar o Valor
        if v == '-19\\|' or v == '-19|\\':
            self.ids.input_value47.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value47.background_color = 1, 0, 0, .5

    def get_score48(self):
        v = str(self.ids.input_value48.text)

        # Verificar o Valor
        if v == '-15\\|' or v == '-15|\\':
            self.ids.input_value48.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value48.background_color = 1, 0, 0, .5

    def get_score49(self):
        v = str(self.ids.input_value49.text)

        # Verificar o Valor
        if v == '-4|':
            self.ids.input_value49.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value49.background_color = 1, 0, 0, .5

    def get_score50(self):
        v = str(self.ids.input_value50.text)

        # Verificar o Valor
        if v == '7\\':
            self.ids.input_value50.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value50.background_color = 1, 0, 0, .5

    def get_score51(self):
        v = str(self.ids.input_value51.text)

        # Verificar o Valor
        if v == '4\\':
            self.ids.input_value51.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value51.background_color = 1, 0, 0, .5

    def get_score52(self):
        v = str(self.ids.input_value52.text)

        # Verificar o Valor
        if v == '-2\\_' or v == '-2_\\':
            self.ids.input_value52.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value52.background_color = 1, 0, 0, .5

    def get_score53(self):
        v = str(self.ids.input_value53.text)
        v1 = str(self.ids.input_value43.text)
        v2 = str(self.ids.input_value44.text)
        v3 = str(self.ids.input_value52.text)

        # Verificar o Valor
        if v == '6\\' and v1 == '1\\' and v2 == '-5\\_' or v2 == '-5_\\' and v3 == '-2\\_' or v3 == '-2_\\':
            self.ids.input_value53.background_color = 0, 5, 0, .5
            self.ids.result_id7.text = '  T'
            self.ids.result_id15.text = '  T'
            self.ids.result_id23.text = '+5'
        else:
            self.ids.input_value53.background_color = 1, 0, 0, .5

    def get_score54(self):
        v = str(self.ids.input_value54.text)

        # Verificar o Valor
        if v == '0_':
            self.ids.input_value54.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value54.background_color = 1, 0, 0, .5

    def get_score55(self):
        v = str(self.ids.input_value55.text)

        # Verificar o Valor
        if v == '-36|':
            self.ids.input_value55.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value55.background_color = 1, 0, 0, .5

    def get_score56(self):
        v = str(self.ids.input_value56.text)

        # Verificar o Valor
        if v == '-25|':
            self.ids.input_value56.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value56.background_color = 1, 0, 0, .5

    def get_score57(self):
        v = str(self.ids.input_value57.text)

        # Verificar o Valor
        if v == '-21\\_' or v == '-21_\\':
            self.ids.input_value57.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value57.background_color = 1, 0, 0, .5

    def get_score58(self):
        v = str(self.ids.input_value58.text)

        # Verificar o Valor
        if v == '-10_':
            self.ids.input_value58.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value58.background_color = 1, 0, 0, .5

    def get_score59(self):
        v = str(self.ids.input_value59.text)

        # Verificar o Valor
        if v == '1|':
            self.ids.input_value59.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value59.background_color = 1, 0, 0, .5

    def get_score60(self):
        v = str(self.ids.input_value60.text)

        # Verificar o Valor
        if v == '5\\':
            self.ids.input_value60.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value60.background_color = 1, 0, 0, .5

    def get_score61(self):
        v = str(self.ids.input_value61.text)

        # Verificar o Valor
        if v == '2\\':
            self.ids.input_value61.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value61.background_color = 1, 0, 0, .5

    def get_score62(self):
        v = str(self.ids.input_value62.text)

        # Verificar o Valor
        if v == '0|':
            self.ids.input_value62.background_color = 0, 0, 1, .5
        else:
            self.ids.input_value62.background_color = 1, 0, 0, .5

    def get_score63(self):
        v = str(self.ids.input_value63.text)
        v1 = str(self.ids.input_value53.text)
        v2 = str(self.ids.input_value54.text)
        v3 = str(self.ids.input_value62.text)

        # Verificar o Valor
        if v == '11\\' and v1 == '6\\' and v2 == '0_' and v3 == '0|':
            self.ids.input_value63.background_color = 0, 5, 0, .5
            self.ids.result_id8.text = '  A'
            self.ids.result_id16.text = '  A'
            self.ids.result_id24.text = '+5'
        else:
            self.ids.input_value63.background_color = 1, 0, 0, .5


class Screen_2_1_1(Screen):
    '''
Classe resposável pela exibição do conteúdo referente a Programação Dinâmica na Bioinformática

'''

    text_back = text_back

    # Abir texto
    text = ''
    with open('data/content/text_dynamicProgramming.txt') as code:
        for line in code:
            text += line


class Screen_2_2(Screen):
    '''
    Classe responsável pelo algoritmos Needleman-Wunsch.

    '''

    text_back = text_back
    text_title_NeedlemanWunsc = text_title_NeedlemanWunsc
    text_sequence_A = text_sequence_A
    text_sequence_B = text_sequence_B
    text_no_nucleotideo_dna = text_no_nucleotideo_dna
    text_no_nucleotideo_rna = text_no_nucleotideo_rna
    text_no_amino_acids = text_no_amino_acids
    text_example_dynamic_NeedlemanWunsch = text_example_dynamic_NeedlemanWunsch
    text_nucleotideo_1 = text_nucleotideo_1  # DNA/RNA
    text_nucleotideo_2 = text_nucleotideo_2
    text_nucleotideo_3 = text_nucleotideo_3
    text_nucleotideo_4 = text_nucleotideo_4
    text_nucleotideo_5 = text_nucleotideo_5
    text_nucleotideo_6 = text_nucleotideo_6
    text_nucleotideo_7 = text_nucleotideo_7
    text_nucleotideo_8 = text_nucleotideo_8
    text_nucleotideo_9 = text_nucleotideo_9
    text_nucleotideo_10 = text_nucleotideo_10
    text_nucleotideo_11 = text_nucleotideo_11
    text_nucleotideo_12 = text_nucleotideo_12
    text_nucleotideo_13 = text_nucleotideo_13
    text_nucleotideo_14 = text_nucleotideo_14
    text_nucleotideo_15 = text_nucleotideo_15
    text_nucleotideo_16 = text_nucleotideo_16
    text_amino_acids_1 = text_amino_acids_1  # Aminoácidos
    text_amino_acids_2 = text_amino_acids_2
    text_amino_acids_3 = text_amino_acids_3
    text_amino_acids_4 = text_amino_acids_4
    text_amino_acids_5 = text_amino_acids_5
    text_amino_acids_6 = text_amino_acids_6
    text_amino_acids_7 = text_amino_acids_7
    text_amino_acids_8 = text_amino_acids_8
    text_amino_acids_9 = text_amino_acids_9
    text_amino_acids_10 = text_amino_acids_10
    text_amino_acids_11 = text_amino_acids_11
    text_amino_acids_12 = text_amino_acids_12
    text_amino_acids_13 = text_amino_acids_13
    text_amino_acids_14 = text_amino_acids_14
    text_amino_acids_15 = text_amino_acids_15
    text_amino_acids_16 = text_amino_acids_16
    text_amino_acids_17 = text_amino_acids_17
    text_amino_acids_18 = text_amino_acids_18
    text_amino_acids_19 = text_amino_acids_19
    text_amino_acids_20 = text_amino_acids_20
    text_spinner_dna = text_spinner_dna
    text_spinner_rna = text_spinner_rna
    text_spinner_amino_acids = text_spinner_amino_acids

    def maximum(c1, c2, up, side, diagonal):
        # A função “maximo" que pega os valores de “c1" e “c2" estão sendo avaliados e pontuam as células como: “lado”, “cima”,“diagonal”
        if (c1 == c2 and (diagonal+1) >= up and (diagonal+1) >= side):
            diagonal = diagonal+1
            return diagonal
        elif (side >= up and side >= diagonal):
            return side
        else:
            return up

    def pointer(c1, c2, up, side, diagonal):
        # A função “ponteiro” é praticamente idêntica à função “maximo” com o diferencial de retornar símbolos “|”, “_” e “\”.
        if (c1 == c2 and (diagonal+1) >= up and (diagonal+1) >= side):
            return '\\'
        elif (side >= up and side >= diagonal):
            return '_'
        else:
            return '|'

    def generateAlignment(v, w, punctuation, pointers):
        # A função gera a matriz de programação dinâmica
        ali_v = ''
        ali_w = ''

        i = len(w)-1
        j = len(v)-1

        while ((i != 0) or (j != 0)):
            if (pointers[i][j] == '\\'):
                ali_v = v[j] + ali_v
                ali_w = w[i] + ali_w
                i -= 1
                j -= 1
            elif (pointers[i][j] == '_'):
                ali_v = v[j] + ali_v
                ali_w = '_' + ali_w
                j -= 1

            else:
                ali_v = '_' + ali_v
                ali_w = w[i] + ali_w
                i -= 1

        return {1: (punctuation[len(w)-1][len(v)-1]), 2: ali_v, 3: ali_w}

    def printMatrix(v, w, punctuation, pointers):
        # A função imprime a matriz de programação dinâmica
        print()
        print(30*'=-=')
        print()
        print(text_example_dynamic_NeedlemanWunsch)
        print()
        print('\t', end='')

        for j in range(0, len(v)):
            print(v[j], end='\t')

        print()

        for i in range(0, len(w)):
            print(w[i], end='\t')
            for j in range(0, len(v)):
                print(punctuation[i][j], pointers[i][j], end='\t', sep='')
            print()

        print()

    def lcs(self):
        # A função lcs "Longest Common Subsequence"
        seq_1 = self.ids.input_1.text
        seq_2 = self.ids.input_2.text

        # Converter em maiscúlo
        seq_1 = seq_1.swapcase()
        seq_2 = seq_2.swapcase()

        # Começar uma Lista
        v = ['*']
        w = ['*']

        # Adicionar de forma individual valor recebido Text Input
        for i in seq_1:
            v.append(i)

        for i in seq_2:
            w.append(i)

        # Ativar ou Desativar o TextInput
        if len(v) < len(w):
            self.ids.input_2.disabled = True
        elif len(v) > len(w):
            self.ids.input_2.disabled = False

        # Variáveis
        punctuation = []
        pointers = []
        punctuation = [0]*len(v)
        pointers = ['']*len(v)

        for i in range(0, len(w)):
            punctuation[i] = [0]*len(v)
            pointers[i] = ['']*len(v)

        for i in range(0, len(w)):
            pointers[i][0] = '|'

        for j in range(0, len(v)):
            pointers[0][j] = '_'

        for i in range(1, len(w)):
            for j in range(1, len(v)):
                punctuation[i][j] = Screen_2_2.maximum(
                    v[j], w[i], punctuation[i-1][j], punctuation[i][j-1], punctuation[i-1][j-1])
                pointers[i][j] = Screen_2_2.pointer(
                    v[j], w[i], punctuation[i-1][j], punctuation[i][j-1], punctuation[i-1][j-1])

        # Enviando para as funações citadas
        Screen_2_2.printMatrix(v, w, punctuation, pointers)
        result = (Screen_2_2.generateAlignment(v, w, punctuation, pointers))

        # Enviar resultado para Tela do Aplicativo
        self.ids.result_1.text = str(result[1])
        self.ids.result_2.text = str(result[2] + '\n' + result[3])

    def keyboard_textInput(self):
        seq = self.ids.input_1.text

        # Adicionar de forma individual valor recebido Text Input
        for i in seq:
            Screen_2_2.check(self, i)

    def keyboard_textInput2(self):
        seq = self.ids.input_2.text

        # Adicionar de forma individual valor recebido Text Input
        for i in seq:
            Screen_2_2.check(self, i)

    def check(self, value):
        # A função "check" pega valores e checa se o caracter é um nuleotídeo ou aminoácido.

        n = value.swapcase()

        # Pegar valor do Spiner quer altera DNA, RNA ou Aminoácidos
        var_spiner = self.ids.spinner_id.text

        # Verificar qual cadeia deve ser inserida
        if var_spiner == text_spinner_dna:
            # DNA
            if n == 'A' or n == 'a':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_1
            elif n == 'C' or n == 'c':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_2
            elif n == 'G' or n == 'g':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_3
            elif n == 'T' or n == 't':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_4
            elif n == 'R' or n == 'r':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_6
            elif n == 'Y' or n == 'y':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_7
            elif n == 'M' or n == 'm':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_8
            elif n == 'K' or n == 'k':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_9
            elif n == 'W' or n == 'w':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_10
            elif n == 'S' or n == 's':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_11
            elif n == 'B' or n == 'b':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_12
            elif n == 'D' or n == 'd':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_13
            elif n == 'H' or n == 'h':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_14
            elif n == 'V' or n == 'v':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_15
            elif n == 'N' or n == 'n':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_16
            else:
                self.ids.no_nucleotideo.text = '[color=#ff0000]' + \
                    n + '[/color]' + ' = ' + text_no_nucleotideo_dna

        elif var_spiner == text_spinner_rna:
            # RNA
            if n == 'A' or n == 'a':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_1
            elif n == 'C' or n == 'c':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_2
            elif n == 'G' or n == 'g':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_3
            elif n == 'U' or n == 'u':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_5
            elif n == 'R' or n == 'r':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_6
            elif n == 'Y' or n == 'y':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_7
            elif n == 'M' or n == 'm':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_8
            elif n == 'K' or n == 'k':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_9
            elif n == 'W' or n == 'w':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_10
            elif n == 'S' or n == 's':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_11
            elif n == 'B' or n == 'b':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_12
            elif n == 'D' or n == 'd':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_13
            elif n == 'H' or n == 'h':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_14
            elif n == 'N' or n == 'n':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_16
            else:
                self.ids.no_nucleotideo.text = '[color=#ff0000]' + \
                    n + '[/color]' + ' = ' + text_no_nucleotideo_rna

        elif var_spiner == text_spinner_amino_acids:
            # Aminoácidos
            if n == 'G' or n == 'g':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_1
            elif n == 'A' or n == 'a':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_2
            elif n == 'L' or n == 'l':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_3
            elif n == 'V' or n == 'v':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_4
            elif n == 'I' or n == 'i':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_5
            elif n == 'P' or n == 'p':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_6
            elif n == 'F' or n == 'f':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_7
            elif n == 'S' or n == 's':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_8
            elif n == 'T' or n == 't':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_9
            elif n == 'C' or n == 'c':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_10
            elif n == 'Y' or n == 'y':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_11
            elif n == 'N' or n == 'n':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_12
            elif n == 'Q' or n == 'q':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_13
            elif n == 'D' or n == 'd':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_14
            elif n == 'E' or n == 'e':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_15
            elif n == 'R' or n == 'r':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_16
            elif n == 'K' or n == 'k':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_17
            elif n == 'H' or n == 'h':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_18
            elif n == 'W' or n == 'w':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_19
            elif n == 'M' or n == 'm':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_20
            else:
                self.ids.no_nucleotideo.text = '[color=#ff0000]' + \
                    n + '[/color]' + ' = ' + text_no_amino_acids


class Screen_2_2_1(Screen):
    '''
    Classe responsável em mostrar código em python do Algoritmo do Needleman-Wunsch

    '''

    text_back = text_back

    # Abir  o código de examplo do código em BioPython na execução do BLAST
    text = ''
    with open('data/content/example_needleman_wunsch.txt') as code:
        for line in code:
            text += line


class Screen_2_3(Screen):
    '''
    Classe responsável pelo algoritmos Smith-Waterman.

    '''

    text_back = text_back
    text_title_SmithWaterman = text_title_SmithWaterman
    text_sequence_A = text_sequence_A
    text_sequence_B = text_sequence_B
    text_no_nucleotideo_dna = text_no_nucleotideo_dna
    text_no_nucleotideo_rna = text_no_nucleotideo_rna
    text_no_amino_acids = text_no_amino_acids
    text_example_dynamic_SmithWaterman = text_example_dynamic_SmithWaterman
    text_nucleotideo_1 = text_nucleotideo_1  # DNA/RNA
    text_nucleotideo_2 = text_nucleotideo_2
    text_nucleotideo_3 = text_nucleotideo_3
    text_nucleotideo_4 = text_nucleotideo_4
    text_nucleotideo_5 = text_nucleotideo_5
    text_nucleotideo_6 = text_nucleotideo_6
    text_nucleotideo_7 = text_nucleotideo_7
    text_nucleotideo_8 = text_nucleotideo_8
    text_nucleotideo_9 = text_nucleotideo_9
    text_nucleotideo_10 = text_nucleotideo_10
    text_nucleotideo_11 = text_nucleotideo_11
    text_nucleotideo_12 = text_nucleotideo_12
    text_nucleotideo_13 = text_nucleotideo_13
    text_nucleotideo_14 = text_nucleotideo_14
    text_nucleotideo_15 = text_nucleotideo_15
    text_nucleotideo_16 = text_nucleotideo_16
    text_amino_acids_1 = text_amino_acids_1  # Aminoácidos
    text_amino_acids_2 = text_amino_acids_2
    text_amino_acids_3 = text_amino_acids_3
    text_amino_acids_4 = text_amino_acids_4
    text_amino_acids_5 = text_amino_acids_5
    text_amino_acids_6 = text_amino_acids_6
    text_amino_acids_7 = text_amino_acids_7
    text_amino_acids_8 = text_amino_acids_8
    text_amino_acids_9 = text_amino_acids_9
    text_amino_acids_10 = text_amino_acids_10
    text_amino_acids_11 = text_amino_acids_11
    text_amino_acids_12 = text_amino_acids_12
    text_amino_acids_13 = text_amino_acids_13
    text_amino_acids_14 = text_amino_acids_14
    text_amino_acids_15 = text_amino_acids_15
    text_amino_acids_16 = text_amino_acids_16
    text_amino_acids_17 = text_amino_acids_17
    text_amino_acids_18 = text_amino_acids_18
    text_amino_acids_19 = text_amino_acids_19
    text_amino_acids_20 = text_amino_acids_20
    text_spinner_dna = text_spinner_dna
    text_spinner_rna = text_spinner_rna
    text_spinner_amino_acids = text_spinner_amino_acids

    def maximum(c1, c2, up, side, diagonal):
        # A função “maximo" que pega os valores de “c1" e “c2" estão sendo avaliados e pontuam as células como: “lado”, “cima”,“diagonal”
        if (c1 == c2 and (diagonal+1) >= up and (diagonal+1) >= side):
            diagonal = diagonal+1
            return diagonal
        elif (side >= up and side >= diagonal):
            return side
        else:
            return up

    def pointer(c1, c2, up, side, diagonal):
        # A função “ponteiro” é praticamente idêntica à função “maximo” com o diferencial de retornar símbolos “|”, “_” e “\”.
        if (c1 == c2 and (diagonal+1) >= up and (diagonal+1) >= side):
            return '\\'
        elif (side >= up and side >= diagonal):
            return '_'
        else:
            return '|'

    def generateAlignment(v, w, punctuation, pointers):
        # A função gera a matriz de programação dinâmica
        ali_v = ''
        ali_w = ''

        i = len(w)-1
        j = len(v)-1

        while ((i != 0) or (j != 0)):
            if (pointers[i][j] == '\\'):
                ali_v = v[j] + ali_v
                ali_w = w[i] + ali_w
                i -= 1
                j -= 1
            elif (pointers[i][j] == '_'):
                ali_v = v[j] + ali_v
                ali_w = '_' + ali_w
                j -= 1

            else:
                ali_v = '_' + ali_v
                ali_w = w[i] + ali_w
                i -= 1

        return {1: (punctuation[len(w)-1][len(v)-1]), 2: ali_v, 3: ali_w}

    def printMatrix(v, w, punctuation, pointers):
        # A função imprime a matriz de programação dinâmica
        print()
        print(30*'=-=')
        print()
        print(text_example_dynamic_SmithWaterman)
        print()
        print('\t', end='')

        for j in range(0, len(v)):
            print(v[j], end='\t')

        print()

        for i in range(0, len(w)):
            print(w[i], end='\t')
            for j in range(0, len(v)):
                print(punctuation[i][j], pointers[i][j], end='\t', sep='')
            print()

        print()

    def matrixPointer_BLOSUM(self):
        #
        pass

    def lcs(self):
        # A função lcs "Longest Common Subsequence"
        seq_1 = self.ids.input_1.text
        seq_2 = self.ids.input_2.text

        # Converter em maiscúlo
        seq_1 = seq_1.swapcase()
        seq_2 = seq_2.swapcase()

        # Começar uma Lista
        v = ['*']
        w = ['*']

        # Adicionar de forma individual valor recebido Text Input
        for i in seq_1:
            v.append(i)

        for i in seq_2:
            w.append(i)

        # Ativar ou Desativar o TextInput
        if len(v) < len(w):
            self.ids.input_2.disabled = True
        elif len(v) > len(w):
            self.ids.input_2.disabled = False

        # Variáveis
        punctuation = []
        pointers = []
        punctuation = [0]*len(v)
        pointers = ['']*len(v)

        for i in range(0, len(w)):
            punctuation[i] = [0]*len(v)
            pointers[i] = ['']*len(v)

        for i in range(0, len(w)):
            pointers[i][0] = '|'

        for j in range(0, len(v)):
            pointers[0][j] = '_'

        for i in range(1, len(w)):
            for j in range(1, len(v)):
                punctuation[i][j] = Screen_2_3.maximum(
                    v[j], w[i], punctuation[i-1][j], punctuation[i][j-1], punctuation[i-1][j-1])
                pointers[i][j] = Screen_2_3.pointer(
                    v[j], w[i], punctuation[i-1][j], punctuation[i][j-1], punctuation[i-1][j-1])

        # Enviando para as funações citadas
        Screen_2_3.printMatrix(v, w, punctuation, pointers)
        result = (Screen_2_3.generateAlignment(v, w, punctuation, pointers))

        # Enviar resultado para Tela do Aplicativo
        self.ids.result_1.text = str(result[1])
        self.ids.result_2.text = str(result[2] + '\n' + result[3])

    def keyboard_textInput(self):
        seq = self.ids.input_1.text

        # Adicionar de forma individual valor recebido Text Input
        for i in seq:
            Screen_2_3.check(self, i)

    def keyboard_textInput2(self):
        seq = self.ids.input_2.text

        # Adicionar de forma individual valor recebido Text Input
        for i in seq:
            Screen_2_3.check(self, i)

    def check(self, value):
        # A função "check" pega valores e checa se o caracter é um nuleotídeo ou aminoácido.

        n = value.swapcase()

        # Pegar valor do Spiner quer altera DNA, RNA ou Aminoácidos
        var_spiner = self.ids.spinner_id.text

        # Verificar qual cadeia deve ser inserida
        if var_spiner == text_spinner_dna:
            # DNA
            if n == 'A' or n == 'a':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_1
            elif n == 'C' or n == 'c':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_2
            elif n == 'G' or n == 'g':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_3
            elif n == 'T' or n == 't':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_4
            elif n == 'R' or n == 'r':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_6
            elif n == 'Y' or n == 'y':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_7
            elif n == 'M' or n == 'm':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_8
            elif n == 'K' or n == 'k':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_9
            elif n == 'W' or n == 'w':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_10
            elif n == 'S' or n == 's':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_11
            elif n == 'B' or n == 'b':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_12
            elif n == 'D' or n == 'd':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_13
            elif n == 'H' or n == 'h':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_14
            elif n == 'V' or n == 'v':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_15
            elif n == 'N' or n == 'n':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_16
            else:
                self.ids.no_nucleotideo.text = '[color=#ff0000]' + \
                    n + '[/color]' + ' = ' + text_no_nucleotideo_dna

        elif var_spiner == text_spinner_rna:
            # RNA
            if n == 'A' or n == 'a':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_1
            elif n == 'C' or n == 'c':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_2
            elif n == 'G' or n == 'g':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_3
            elif n == 'U' or n == 'u':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_5
            elif n == 'R' or n == 'r':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_6
            elif n == 'Y' or n == 'y':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_7
            elif n == 'M' or n == 'm':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_8
            elif n == 'K' or n == 'k':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_9
            elif n == 'W' or n == 'w':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_10
            elif n == 'S' or n == 's':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_11
            elif n == 'B' or n == 'b':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_12
            elif n == 'D' or n == 'd':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_13
            elif n == 'H' or n == 'h':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_14
            elif n == 'N' or n == 'n':
                self.ids.no_nucleotideo.text = n + ' = ' + text_nucleotideo_16
            else:
                self.ids.no_nucleotideo.text = '[color=#ff0000]' + \
                    n + '[/color]' + ' = ' + text_no_nucleotideo_rna

        elif var_spiner == text_spinner_amino_acids:
            # Aminoácidos
            if n == 'G' or n == 'g':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_1
            elif n == 'A' or n == 'a':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_2
            elif n == 'L' or n == 'l':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_3
            elif n == 'V' or n == 'v':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_4
            elif n == 'I' or n == 'i':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_5
            elif n == 'P' or n == 'p':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_6
            elif n == 'F' or n == 'f':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_7
            elif n == 'S' or n == 's':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_8
            elif n == 'T' or n == 't':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_9
            elif n == 'C' or n == 'c':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_10
            elif n == 'Y' or n == 'y':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_11
            elif n == 'N' or n == 'n':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_12
            elif n == 'Q' or n == 'q':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_13
            elif n == 'D' or n == 'd':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_14
            elif n == 'E' or n == 'e':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_15
            elif n == 'R' or n == 'r':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_16
            elif n == 'K' or n == 'k':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_17
            elif n == 'H' or n == 'h':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_18
            elif n == 'W' or n == 'w':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_19
            elif n == 'M' or n == 'm':
                self.ids.no_nucleotideo.text = n + ' = ' + text_amino_acids_20
            else:
                self.ids.no_nucleotideo.text = '[color=#ff0000]' + \
                    n + '[/color]' + ' = ' + text_no_amino_acids


class Screen_2_3_1(Screen):
    '''
Classe resposável pela exibição do código do Smith-Waterman em BioPython

'''

    text_back = text_back

    # Abir  o código de examplo do código do algoritmo Smith-Waterman
    text = ''
    with open('data/content/example_smith_waterman.txt') as code:
        for line in code:
            text += line


class Screen_2_4(Screen):
    '''
    Classe resposável pela execução do BLAST

    '''
    text_title_blast = text_title_blast
    text_sequence_A = text_sequence_A
    text_sequence_B = text_sequence_B
    text_blast = text_blast
    text_mensage_error = text_mensage_error
    text_spinner_blastn = text_spinner_blastn
    text_spinner_blastp = text_spinner_blastp
    text_spinner_blastx = text_spinner_blastx
    text_spinner_tblastn = text_spinner_tblastn
    text_spinner_tblastx = text_spinner_tblastx
    text_back = text_back

    def keyboard_textInput(self):
        # Função responsável pela busca no site
        seq1 = self.ids.input_sequence_A.text
        seq2 = self.ids.input_sequence_B.text

        # Variáveis carregadas no Módulo IUPAC
        dna2 = Seq(seq2)
        dna1 = Seq(seq1)

        # Gravar as sequências em fasta
        file = open('data/tmp/sequence_A.fasta', 'w')
        file.writelines('>\n' + str(dna1))
        file.close()

        file = open('data/tmp/sequence_B.fasta', 'w')
        file.writelines('>\n' + str(dna2))
        file.close()

    def button_blast(self):
        # Pegar valor do Spiner quer altera DNA, RNA ou Aminoácidos
        var_spiner = self.ids.spinner_id.text

        # Executar o BLAST
        try:
            if 'BLASTn' == var_spiner:
                comando_blastn = NcbiblastnCommandline(
                    query="data/tmp/sequence_A.fasta", subject="data/tmp/sequence_B.fasta", outfmt=0)
                stdout, stderr = comando_blastn()
                # Mensagem da tela
                self.ids.information_id.text = ''
                # Gravar o resultado do Blast
                file = open('data/tmp/Result_BLASTN.fasta', 'w')
                file.writelines(stdout)
                file.writelines(stderr)
                file.close()
                # Exibir o resultado na Tela
                webbrowser.open('data/tmp/Result_BLASTN.fasta',
                                new=0, autoraise=True)
            elif 'BLASTp' == var_spiner:
                comando_blastn = NcbiblastpCommandline(
                    query="data/tmp/sequence_A.fasta", subject="data/tmp/sequence_B.fasta", outfmt=0)
                stdout, stderr = comando_blastn()
                # Mensagem da tela
                self.ids.information_id.text = ''
                # Gravar o resultado do Blast
                file = open('data/tmp/Result_BLASTN.fasta', 'w')
                file.writelines(stdout)
                file.writelines(stderr)
                file.close()
                # Exibir o resultado na Tela
                webbrowser.open('data/tmp/Result_BLASTN.fasta',
                                new=0, autoraise=True)
            elif 'BLASTx' == var_spiner:
                comando_blastn = NcbiblastxCommandline(
                    query="data/tmp/sequence_A.fasta", subject="data/tmp/sequence_B.fasta", outfmt=0)
                stdout, stderr = comando_blastn()
                # Mensagem da tela
                self.ids.information_id.text = ''
                # Gravar o resultado do Blast
                file = open('data/tmp/Result_BLASTN.fasta', 'w')
                file.writelines(stdout)
                file.writelines(stderr)
                file.close()
                # Exibir o resultado na Tela
                webbrowser.open('data/tmp/Result_BLASTN.fasta',
                                new=0, autoraise=True)
            elif 'tBLASTn' == var_spiner:
                comando_blastn = NcbitblastnCommandline(
                    query="data/tmp/sequence_A.fasta", subject="data/tmp/sequence_B.fasta", outfmt=0)
                stdout, stderr = comando_blastn()
                # Mensagem da tela
                self.ids.information_id.text = ''
                # Gravar o resultado do Blast
                file = open('data/tmp/Result_BLASTN.fasta', 'w')
                file.writelines(stdout)
                file.writelines(stderr)
                file.close()
                # Exibir o resultado na Tela
                webbrowser.open('data/tmp/Result_BLASTN.fasta',
                                new=0, autoraise=True)
            elif 'tBLASTx' == var_spiner:
                comando_blastn = NcbitblastxCommandline(
                    query="data/tmp/sequence_A.fasta", subject="data/tmp/sequence_B.fasta", outfmt=0)
                stdout, stderr = comando_blastn()
                # Mensagem da tela
                self.ids.information_id.text = ''
                # Gravar o resultado do Blast
                file = open('data/tmp/Result_BLASTN.fasta', 'w')
                file.writelines(stdout)
                file.writelines(stderr)
                file.close()
                # Exibir o resultado na Tela
                webbrowser.open('data/tmp/Result_BLASTN.fasta',
                                new=0, autoraise=True)
        except:
            # Popup
            layout = BoxLayout(orientation='vertical',
                               spacing=20, padding=[20, 20, 20, 20])
            label = Label(text=self.text_mensage_error,
                          halign='left', markup=True)
            button_close = Button(text='OK', size_hint_y=None, height=48, background_color=(
                1, 0, 0, 1), background_normal=(''), background_down=(''))
            layout.add_widget(label)
            layout.add_widget(button_close)
            popup = Popup(title='Error', content=layout, size_hint=(None, None), size=(
                100, 100), background='atlas://data/images/defaulttheme/button_pressed')
            button_close.bind(on_press=popup.dismiss)
            animation = Animation(size=(300, 250), duration=0.3, t='out_back')
            animation.start(popup)
            popup.open()


class Screen_2_4_1(Screen):
    '''
    Classe resposável pela exibição do código do BLAST em BioPython

    '''

    text_back = text_back

    # Abir  o código de examplo do código em BioPython na execução do BLAST
    text = ''
    with open('data/content/example_code_blast.txt') as code:
        for line in code:
            text += line

    text2 = ''
    with open('data/content/text_blast.txt') as code:
        for line in code:
            text2 += line


class Screen_3(Screen):
    '''
    Classe reponsável pela Tela de Vacabulário do ACTG_go!
    '''
    text_back = text_back

    # Abir o texto
    text = ''
    with open('data/content/text_vacabulary.txt') as code:
        for line in code:
            text += line


# Definir nomes para Telas
screen_manager = ScreenManager()
screen_manager.add_widget(Screen_Splash(name="splash"))
screen_manager.add_widget(Screen_Menu(name="menu"))
screen_manager.add_widget(Screen_1(name="screen_1"))
screen_manager.add_widget(Screen_1_1(name="screen_1_1"))
screen_manager.add_widget(Screen_2(name="screen_2"))
screen_manager.add_widget(Screen_2_1(name="screen_2_1"))
screen_manager.add_widget(Screen_2_1_1(name="screen_2_1_1"))
screen_manager.add_widget(Screen_2_2(name="screen_2_2"))
screen_manager.add_widget(Screen_2_2_1(name="screen_2_2_1"))
screen_manager.add_widget(Screen_2_3(name="screen_2_3"))
screen_manager.add_widget(Screen_2_3_1(name="screen_2_3_1"))
screen_manager.add_widget(Screen_2_4(name="screen_2_4"))
screen_manager.add_widget(Screen_2_4_1(name="screen_2_4_1"))
screen_manager.add_widget(Screen_3(name="screen_3"))


# Classe principal
class MainApp(App):

    title = "ATCG_go!"

    def build(self):
        return screen_manager


if __name__ == '__main__':
    MainApp().run()
