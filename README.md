# Gamificação de Estudo: Aplicativo de Desafios Diários

## Visão Geral do Projeto

Este projeto visa criar uma plataforma de gamificação para incentivar e acompanhar a rotina de estudos dos usuários [1]. O aplicativo permite que os usuários criem desafios de estudo (individualmente ou com amigos), estabeleçam metas diárias e mensais, e compitam através de um sistema de pontos e ranking [1, 2]. O diferencial inclui a validação do conhecimento absorvido por meio de perguntas geradas por Inteligência Artificial [1, 3].

## Funcionalidades Principais

*   **Criação e Gestão de Desafios** [1]:
    *   Usuários podem criar novos desafios de estudo, definindo a duração (mensal) e a frequência de dias de estudo por semana (ex: 5 dias/semana) [1, 2].
    *   Participação em desafios existentes, com foco na dinâmica com amigos [1].
*   **Registro Diário de Estudo** [1, 4]:
    *   Registro do que foi estudado no dia (descrição), tempo dedicado ao estudo e upload de uma foto do ambiente de estudo. A foto serve como prova visual do engajamento, sem validação rigorosa inicial [1, 4].
    *   Marcação do dia como concluído após o registro.
*   **Validação de Conhecimento por IA** [1, 3]:
    *   Após o registro diário, uma IA (integrada com n8n) formula perguntas baseadas no resumo do conteúdo estudado pelo usuário [1, 3].
    *   As respostas a essas perguntas são utilizadas para validar o "conhecimento absorvido" e atribuir pontos diários (ex: 5 pontos para a nota máxima por dia) [3].
*   **Sistema de Pontuação e Ranking** [1, 2]:
    *   Pontos diários são acumulados e somados no final do mês para um ranking geral, determinando um vencedor no desafio [1].
    *   O tempo estudado pode ser um fator secundário na pontuação, mas é uma meta mínima configurável no desafio [2].
*   **Notificações** [1]:
    *   Notificações da IA para solicitar a validação diária do conteúdo estudado.

## Tecnologias Utilizadas

Este projeto é uma aplicação full-stack, construída com as seguintes tecnologias:

*   **Banco de Dados (Database)**:
    *   **PostgreSQL**: Um poderoso sistema de banco de dados relacional e de código aberto [usuário]. PostgreSQL oferece recursos robustos de replicação (como a replicação baseada em líder) [5] e é conhecido por sua confiabilidade e conformidade com padrões SQL.
*   **Backend**:
    *   **Node.js**: Um ambiente de tempo de execução JavaScript que permite a construção de aplicações de servidor eficientes e escaláveis [usuário, 174]. Será utilizado para a lógica de negócio, interação com o banco de dados e integração com a IA (n8n) [6, 7].
*   **Frontend**:
    *   **HTML (HyperText Markup Language)**: A linguagem padrão para estruturar o conteúdo da web [8, 9]. Utilizará tags semânticas HTML5 para criar uma estrutura clara e acessível para a interface do usuário [10]. Elementos como formulários, tabelas e listas serão fundamentais para a apresentação dos desafios e dados de estudo [11-14].
    *   **CSS (Cascading Style Sheets)**: Usado para descrever o estilo e a apresentação dos documentos HTML [8, 9]. Permitirá a estilização de fontes, cores, layouts (como Flexbox e Grid) e o modelo de caixa (Box Model) para um design responsivo e visualmente atraente [15-22].
    *   **JavaScript**: Uma linguagem de script de propósito geral para adicionar interatividade e comportamento dinâmico ao frontend [8, 9, 23]. Será essencial para a manipulação do Document Object Model (DOM) [24, 25], gerenciamento de eventos, funções e lógica do lado do cliente que interage com o backend [26-28].

## Estrutura do Projeto (Sugestão)

O projeto pode ser organizado da seguinte forma para separar as responsabilidades do frontend e backend:

my-gamified-study-app/ ├── backend/                  # Aplicação Node.js (API, lógica de negócio) │   ├── src/                  # Código-fonte da aplicação (controllers, models, services) │   ├── config/               # Configurações do banco de dados e outros serviços │   ├── database/             # Migrações e seeds do PostgreSQL │   ├── node_modules/ │   ├── package.json │   └── server.js             # Ponto de entrada do backend ├── frontend/                 # Aplicação HTML, CSS, JavaScript │   ├── index.html            # Página principal │   ├── css/                  # Arquivos CSS (style.css, componentes) │   ├── js/                   # Arquivos JavaScript (lógica do cliente, interações com a API) │   └── assets/               # Imagens, fontes e outros recursos estáticos ├── docs/                     # Documentação adicional do projeto └── README.md                 # Este arquivo

## Configuração e Instalação

Para configurar e executar o projeto localmente, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:

*   **Node.js** e **npm** (ou yarn)
*   **PostgreSQL**
*   **Git**

### Passos

1.  **Clonar o Repositório**:
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd my-gamified-study-app
    ```
2.  **Configurar o Banco de Dados PostgreSQL**:
    *   Crie um novo banco de dados PostgreSQL para o projeto.
    *   Anote as credenciais (usuário, senha, nome do banco, porta).
    *   Execute os scripts SQL ou migrações localizados em `backend/database/` para criar as tabelas necessárias.
3.  **Configurar o Backend**:
    ```bash
    cd backend
    npm install
    ```
    *   Crie um arquivo `.env` na raiz do diretório `backend` e adicione as variáveis de ambiente necessárias para a conexão com o PostgreSQL e as configurações da IA (n8n). Exemplo:
        ```
        DB_HOST=localhost
        DB_USER=your_user
        DB_PASSWORD=your_password
        DB_NAME=your_database_name
        DB_PORT=5432
        N8N_WEBHOOK_URL=your_n8n_webhook_url_for_ia_validation
        ```
    *   Inicie o servidor backend:
        ```bash
        npm start
        ```
        O backend estará disponível em `http://localhost:3000` (ou outra porta configurada).
4.  **Configurar o Frontend**:
    ```bash
    cd ../frontend
    ```
    *   Para aplicações HTML/CSS/JS puras, basta abrir o arquivo `index.html` em seu navegador web.
    *   Se estiver utilizando um servidor de desenvolvimento local (como o Live Server para VS Code), inicie-o no diretório `frontend`.

## Como Usar

1.  **Acessar o Aplicativo**: Abra o `index.html` no seu navegador (ou a URL do servidor de desenvolvimento).
2.  **Criar/Participar de Desafios**: Navegue pela interface para criar seu primeiro desafio de estudo ou junte-se a um já existente com seus amigos.
3.  **Registrar Estudo Diário**: Preencha o formulário diário com o que você estudou, o tempo dedicado e uma foto do seu local de estudo.
4.  **Validação da IA**: Acompanhe as notificações da IA para responder às perguntas e validar seu aprendizado.
5.  **Acompanhar o Progresso**: Verifique seu painel de controle para ver seus pontos e sua posição no ranking mensal.

## Diretrizes de Desenvolvimento

Para garantir a qualidade, manutenção e escalabilidade do projeto, recomendamos aderir aos seguintes princípios:

*   **Código Limpo (Clean Code)** [29]:
    *   **Nomes Significativos**: Use nomes claros e concisos para variáveis, funções e classes que revelem sua intenção [30]. Evite nomes genéricos ou abreviações obscuras [31, 32].
    *   **Funções Pequenas e Únicas**: Cada função deve ter uma única responsabilidade (Princípio da Responsabilidade Única - SRP) e ser o menor possível [33-36].
    *   **Evitar Efeitos Colaterais**: Funções devem produzir os resultados esperados sem alterações inesperadas no estado do sistema [37].
    *   **Sem Repetição (DRY - Don't Repeat Yourself)**: Evite duplicar código. Se uma lógica é usada mais de uma vez, ela deve ser abstraída em uma função ou módulo reutilizável [38, 39].
*   **Documentação**:
    *   Mantenha o `README.md` e outras documentações atualizadas e concisas [40].
    *   Comentários no código devem explicar o "porquê" (a intenção, as decisões de design, os *trade-offs*) e não o "o quê" (o código em si) [41, 42].
*   **Testes** [18, 43, 44]:
    *   Implemente testes de unidade, integração e end-to-end. O "Código Limpo" enfatiza que testes devem ser fáceis de ler, rápidos de executar, independentes, repetíveis, e auto-validáveis (F.I.R.S.T. principle) [45].
    *   Testes ajudam a garantir a correção do sistema e a proteger contra degradações futuras [46].
*   **Comunicação**:
    *   Fomente a comunicação clara e eficaz dentro da equipe e com os stakeholders, seguindo os princípios de um programador pragmático [47, 48].
*   **Modularidade**:
    *   Organize o código em módulos com responsabilidades bem definidas para facilitar a manutenção e a reutilização.

## Próximos Passos e Considerações Futuras

Com base nas reflexões sobre gamificação [49], aqui estão algumas áreas para aprofundamento e melhoria contínua:

*   **Qualidade e Relevância das Perguntas da IA**:
    *   É crucial definir como a IA garantirá a qualidade e a relevância das perguntas, bem como a avaliação da profundidade das respostas para uma pontuação justa [49].
    *   Implementar um mecanismo de feedback para que a IA possa refinar e melhorar a geração de perguntas ao longo do tempo [49].
*   **Experiência do Usuário com o Sistema de Pontuação**:
    *   Reavaliar a complexidade de mecanismos como o "gulag" para recuperar pontos, garantindo que adicionem valor sem frustrar o usuário [49]. Considerar "caminhos de revisão guiada" mais simples para conteúdos não validados.
*   **Validação Robusta do Tempo de Estudo**:
    *   Integrar um **cronômetro embutido** no aplicativo que pause automaticamente ao sair ou em caso de inatividade. Isso aumentaria a integridade do registro do tempo e minimizaria entradas fraudulentas [49].
*   **Dinâmica Social e Anti-Trapaça**:
    *   Pensar em estratégias para lidar com trapaças ou validações inconsistentes em um ambiente competitivo com amigos.
    *   Explorar elementos de **cooperação** (além da competição), como bônus para grupos que atingem metas coletivas [49].
*   **Motivação a Longo Prazo**:
    *   Além dos pontos, implementar funcionalidades que incentivem a **motivação intrínseca** e o aprendizado genuíno, como visualização de progresso por tópico, recompensas por sequências de estudo (rachas) ou emblemas por domínio de conteúdo [49].

## Como Contribuir

Agradecemos a todos que desejam contribuir para este projeto! Para contribuir, siga os passos:

1.  Faça um fork do projeto.
2.  Crie uma nova branch (`git checkout -b feature/sua-feature`).
3.  Implemente suas alterações e faça commit (`git commit -m 'feat: Adiciona nova funcionalidade'`). Lembre-se de seguir as diretrizes de desenvolvimento.
4.  Envie suas alterações para o fork (`git push origin feature/sua-feature`).
5.  Abra um Pull Request, descrevendo suas alterações.

## Licença

Este projeto está sob a licença [Nome da Licença, ex: MIT]. Veja o arquivo `LICENSE` para mais detalhes.

---
