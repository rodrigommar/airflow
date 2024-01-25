| Argumento                 | Descrição                                                                                        |
|---------------------------|--------------------------------------------------------------------------------------------------|
| `dag_id`                  | Identificador único da DAG.                                                                      |
| `default_args`            | Dicionário com argumentos padrão aplicados a todas as tarefas.                                   |
| `description`             | Descrição da DAG.                                                                                |
| `schedule_interval`       | Intervalo de agendamento para a execução periódica da DAG (em formato cron ou timedelta).        |
| `start_date`              | Data de início da DAG.                                                                           |
| `end_date`                | Data de término da DAG.                                                                          |
| `catchup`                 | Se True, executa as execuções anteriores que não foram executadas durante o período de ausência. |
| `default_view`            | Define a visualização padrão no webserver ("tree", "graph", "duration", "gantt", ou "landing").  |
| `orientation`             | Orientação da árvore do DAG ("LR" para esquerda-direita, "TB" para cima-baixo).                  |
| `max_active_runs`         | Número máximo de execuções ativas simultaneamente.                                               |
| `user_defined_macros`     | Dicionário de macros definidas pelo usuário para serem disponibilizadas para as tarefas.         |
| `user_defined_filters`    | Dicionário de filtros definidos pelo usuário para serem disponibilizados para as tarefas.        |
| `params`                  | Dicionário de parâmetros que podem ser passados para a DAG.                                      |
| `concurrency`             | Número máximo de execuções concorrentes permitidas.                                              |
| `sla_miss_callback`       | Função chamada quando uma tarefa ultrapassa sua SLA.                                             |
| `on_failure_callback`     | Função chamada quando qualquer tarefa da DAG falha.                                              |
| `on_success_callback`     | Função chamada quando todas as tarefas da DAG têm sucesso.                                       |
| `on_retry_callback`       | Função chamada quando qualquer tarefa da DAG é reexecutada.                                      |
| `tags`                    | Lista de tags associadas à DAG.                                                                  |
| `execution_timeout`       | Tempo limite para a execução de toda a DAG.                                                      |
| `default_args`            | Argumentos padrão aplicados a todas as tarefas.                                                  |
| `doc_md`                  | Documentação Markdown associada à DAG.                                                           |
 