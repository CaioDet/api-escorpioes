
# 🦂 API de Ocorrências de Escorpiões

### 🌐 Projeto Integrador em Computação I — UNIVESP  
**Universidade Virtual do Estado de São Paulo – Polo Hortolândia**  
Curso de **Bacharelado em Ciência de Dados**  
Ano: 2025

---

## 📌 Sobre o Projeto

Este projeto tem como objetivo principal o desenvolvimento de uma **aplicação web interativa** para registro e mapeamento georreferenciado de ocorrências de escorpiões no município de Hortolândia/SP. A proposta visa **modernizar e substituir o atual sistema baseado em ligações telefônicas**, otimizando o trabalho da Vigilância em Saúde e ampliando o acesso da população à informação preventiva e ao controle de zoonoses.

---

## 🎯 Objetivos

### Objetivo Geral
Desenvolver uma ferramenta digital de acesso público para facilitar o registro e visualização de ocorrências de escorpiões, promovendo **comunicação eficiente entre a população e os órgãos públicos**.

### Objetivos Específicos
- Identificar áreas com maior número de casos;
- Facilitar o registro de novas ocorrências por qualquer cidadão;
- Fornecer visualização em **mapa de calor interativo**;
- Melhorar a base de dados para **análise epidemiológica e planejamento estratégico**;
- Promover **conscientização social e educação preventiva**.

---

## 🧠 Fundamentação

A iniciativa surge frente ao aumento de casos de escorpionismo no Brasil, especialmente relacionados ao *Tityus serrulatus* (escorpião-amarelo), associado a maior risco de óbito em crianças. Hortolândia registra anualmente entre 400 e 600 ocorrências. O sistema atual baseado em telefonemas é limitado e dificulta o monitoramento efetivo.

Com base em metodologias quali-quantitativas e princípios de **Design Thinking**, esta aplicação propõe-se a ser um canal de comunicação intuitivo e acessível, com potencial para evoluir futuramente em um **aplicativo educacional e colaborativo**.

---

## 💻 Funcionalidades Atuais

- [x] API REST em Flask para consulta e inserção de dados
- [x] Banco de dados SQLite para persistência local
- [x] Visualização dos registros em **mapa de calor** (Folium)
- [x] Interface para cadastro manual de ocorrências
- [x] Página inicial com rotas acessíveis

---

## 🚀 Acesse a aplicação

- 🦂 Página inicial: [`/home`](https://api-escorpioes.onrender.com/home)  
- 🗺️ Mapa de calor: [`/mapa`](https://api-escorpioes.onrender.com/mapa)  
- ➕ Nova ocorrência: [`/adicionar`](https://api-escorpioes.onrender.com/adicionar)  
- 📄 Ver dados em JSON: [`/ocorrencias`](https://api-escorpioes.onrender.com/ocorrencias)

---

## 🧑‍🤝‍🧑 Equipe

Projeto desenvolvido por alunos da **UNIVESP - Polo Hortolândia**, turma 2025:

- Amanda Pereira Pereira de Deus  
- Antonio Carlos Lepri Junior  
- Caio Vinicius Detoni  
- Jorge Antonio Cruz de Castro  
- Mariana da Conceição Mendes  
- Mateus Vaz Hipólito  
- Mônica Esteves Almeida de Lima  
- Rafhaella Nogueira de Araújo  

**Tutora:** Débora Cristina Oliveira de Souza Neves

---

## 🔮 Próximos Passos

Este é um projeto em fase inicial. Em versões futuras, pretendemos:

- 🔒 Implementar autenticação para agentes autorizados
- 📱 Desenvolver versão mobile responsiva
- 📊 Integrar dashboards de dados e estatísticas
- 🌍 Tornar a ferramenta pública, com banco de dados persistente online (ex: Supabase ou PostgreSQL)
- 👥 Tornar a interface ainda mais **intuitiva para a população**, com orientações e alertas em tempo real

---

## 📄 Licença

Este projeto é de natureza acadêmica e está vinculado às diretrizes da disciplina de Projeto Integrador I da UNIVESP. Pode ser adaptado para uso público sob solicitação.
