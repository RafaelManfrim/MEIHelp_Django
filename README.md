# Requisitos

## Buscar CNPJ

**Requisitos Funcionais**
- [ ] Deve ser possível buscar um CNPJ

**Regra de negócio**
- [ ] Ao buscar, deve salvar no banco
- [ ] Tem validade de 30 dias, caso ultrapasse deverá ser buscado novamente para verificar os dados

## Cadastrar empresa

**Requisitos Funcionais**
- [ ] Deve ser possível cadastrar uma nova empresa

**Regra de negócio**
- [ ] Não deve ser possível cadastrar uma nova empresa com um CNPJ já cadastrado
- [ ] Não deve ser possível cadastrar uma empresa que não for do tipo MEI

## Remover empresa

**Requisitos Funcionais**
- [ ] Deve ser possível remover uma empresa

**Regra de negócio**
- [ ] Não deve ser possível remover uma empresa não cadastrada

## Criação de atividade

**Requisitos Funcionais**
- [ ] O usuário deverá poder criar uma atividade/compromisso

**Regra de negócio**
- [ ] Não deve ser possível uma atividade ser criada pode um usuário não existente

## Edição de atividade

**Requisitos Funcionais**
- [ ] O usuário deverá poder editar uma atividade/compromisso

**Regra de negócio**
- [ ] Não deve ser possível uma atividade ser editada pode um usuário não existente
- [ ] Somente o usuário que criou poderá editar sua atividade

## Conclusão de atividade

**Requisitos Funcionais**
- [ ] O usuário deverá poder concluir uma atividade/compromisso

**Regra de negócio**
- [ ] Não deve ser possível uma atividade ser concluída pode um usuário não existente
- [ ] Somente o usuário que criou poderá concluir sua atividade

## Exclusão de atividade

**Requisitos Funcionais**
- [ ] O usuário deverá poder excluir uma atividade/compromisso

**Regra de negócio**
- [ ] Não deve ser possível uma atividade ser excluída pode um usuário não existente
- [ ] Somente o usuário que criou poderá excluir sua atividade

## Gerar relatórios e gráficos

**Requisitos Funcionais**
- [ ] Deve ser possível gerar relatórios diários, semanais, mensais e anuais de vendas e compras
- [ ] Deve ser possível gerar gráficos de receitas, despesas e lucros


## Stock

- [X] Deve ser possível criar um estoque
- [X] Deverá ser possível listar os estoques criados por um usuário, na listagem deverá vir todos os produtos nesse estoque, e seus respectivos fornecedores
- [X] O nome do estoque poderá ser editado
- [X] Deverá ser possível Excluir um estoque
- [ ] Deverá ser possível adicionar e remover produtos de um estoque
- [ ] Deverá ser possível listar os produtos cadastrados por uma empresa
- [ ] Deverá ser possível cadastrar e editar um produto
- [ ] Deverá ser possível modificar a quantidade de um produto do estoque
- [ ] Deverá ser possível cadastrar e remover fornecedores de um produto
- [ ] Deverá ser possivel listar os fornecedores
- [ ] Deverá ser possível editar os dados de um fornecedor
