# Análise de Documentos Anti-fraude com AzureAI

Implementação de uma solução de análise automatizada de documentos desenvolvida como parte do **Bootcamp Microsoft Certification Challenge #1 - AI 102** da **Digital Innovation One (DIO)**. O objetivo do projeto é utilizar serviços do **Azure AI** para identificar padrões de fraude, validar a autenticidade de documentos e aumentar a segurança em transações e processos empresariais.

## 🌟 Objetivo

Criar um sistema confiável e eficiente para analisar documentos utilizando tecnologias de inteligência artificial fornecidas pelo **Azure AI**, que:

- **Detecte padrões de fraude** em documentos.
- **Valide a autenticidade** de informações.
- **Garanta maior segurança** em transações financeiras e processos empresariais.
- **Aumente a confiabilidade** no processamento de documentos sensíveis.

## 🛠️ Tecnologias Utilizadas

- **Azure AI Document Intelligence**: Para análise e extração de dados de documentos.
- **Python**: Linguagem de programação para implementação do projeto.
- **Streamlit**: Para criar uma interface visual interativa.
- **Azure Blob Storage**: Para armazenar e gerenciar documentos enviados para análise.
- **GitHub**: Controle de versão e hospedagem do projeto.

## 📂 Estrutura do Projeto

- `app.py`: Código principal da aplicação.
- `utils/Config.py`: Configurações do projeto, incluindo variáveis de conexão com o Azure.
- `requirements.txt`: Dependências necessárias para o projeto.
- `README.md`: Documento explicativo sobre o projeto.

## 🚀 Funcionalidades

1. **Upload de Documentos**: Permite o envio de documentos para análise.
2. **Análise Automatizada**: Utiliza o **Azure AI** para detectar inconsistências e padrões de fraude.
3. **Visualização de Resultados**: Exibe os dados analisados e possíveis alertas relacionados a fraudes.
4. **Armazenamento Seguro**: Os documentos enviados são armazenados no **Azure Blob Storage**.

## 🎯 Casos de Uso

- Análise de cartões de crédito para detecção de fraudes.
- Validação de documentos contratuais ou financeiros.
- Identificação de discrepâncias em transações sensíveis.

## 🔧 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/dudaduarte07/-AnaliseDocumentos-AntiFraude
   ```
