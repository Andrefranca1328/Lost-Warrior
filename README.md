# Lost Warrior 🎮

*Um jogo de plataforma 2D de estilo clássico, desenvolvido com Pygame Zero.*

## Sobre o Jogo

Em **Lost Warrior**, você assume o controle de um cavaleiro perdido em uma terra misteriosa, cheia de plataformas flutuantes e inimigos perigosos. O seu objetivo é explorar o cenário, desviar dos perigos e coletar todas as moedas perdidas para encontrar o caminho para casa.

Este projeto foi desenvolvido como um teste de habilidades em Python, seguindo um conjunto estrito de requisitos técnicos e de design.

## ✨ Funcionalidades

* **Menu Principal Interativo:** Com botões para Iniciar o Jogo, Ligar/Desligar a Música e Sair. Os botões possuem feedback visual ao passar o mouse.
* **Personagem com Animação Completa:** O herói possui animações para os estados: parado (idle), correndo, pulando, recebendo dano e morrendo.
* **Inimigos com Patrulha:** O jogo inclui inimigos que se movem em padrões horizontais e verticais.
* **Sistema de Vida e Dano:** O jogador tem um contador de vida visual (corações) e fica temporariamente invencível após ser atingido, com um efeito de "piscar".
* **Moedas Animadas e Objetivo de Coleta:** O objetivo principal é coletar todas as moedas animadas do nível.
* **Música e Efeitos Sonoros:** O jogo conta com música de fundo e efeitos sonoros para pulo, coleta de moedas e dano.

## 🕹️ Como Jogar

* **Seta Esquerda / Direita:** Mover o personagem.
* **Seta Cima:** Pular.
* **Mouse:** Navegar e clicar nos botões do menu.
* **ENTER:** Voltar para o menu após vencer ou perder.

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.x
* Pip (gerenciador de pacotes do Python)

### Instalação e Execução
1.  Clone este repositório ou baixe os arquivos do projeto.
2.  Abra um terminal ou prompt de comando na pasta raiz do projeto.
3.  Instale a biblioteca Pygame Zero:
    ```bash
    pip install pgzero
    ```
4.  Execute o jogo com o seguinte comando:
    ```bash
    pgzrun main.py
    ```

## 🔧 Detalhes Técnicos

Este projeto foi construído seguindo estritamente os requisitos do teste para tutores de Python, utilizando apenas as seguintes bibliotecas:
**PgZero** 

A arquitetura do código é orientada a objetos, com classes customizadas para o `Player`, `Enemy` e `Coin`, conforme solicitado. Todo o código foi escrito de forma independente e segue as convenções do PEP8.

### Estrutura do Projeto
```
lost-warrior/
├── main.py              # Loop principal e gerenciamento do jogo
├── README.md            # Este arquivo
├── classes/
│   ├── player.py        # Lógica do personagem principal
│   ├── enemy.py         # Lógica dos inimigos
│   └── coin.py          # Lógica das moedas animadas
├── images/              # Contém todos os sprites e imagens da UI
├── sounds/              # Contém todos os efeitos sonoros (.wav)
├── music/               # Contém a música de fundo (.mp3)
└── fonts/               # Contém os arquivos de fonte (.ttf)
```

---

Criado por: **ANDRÉ LUIZ DE FRANÇA JUNIOR**
