# Método dos Mínimos Quadrados

Parte do curso
[Matemática Especial I](http://www.leouieda.com/matematica-especial/)
da [UERJ](http://www.uerj.br/).

Ministrado por [Leonardo Uieda](http://www.leouieda.com/).

## Objetivos

* Aprender a formulação matricial do método dos mínimos quadrados (MMQ)
* Treinar o uso de funções e programação defensiva
* Utilizar o MMQ para ajustar uma reta a dados ruidosos
* Generalizar o MMQ para qualquer função linear

## Leitura recomendada

* https://en.wikipedia.org/wiki/Least_squares
* https://en.wikipedia.org/wiki/Linear_least_squares_%28mathematics%29
* http://www.mat.ufmg.br/gaal/aplicacoes/quadrados_minimos.pdf
* https://pt.wikipedia.org/wiki/M%C3%A9todo_dos_m%C3%ADnimos_quadrados

## Preparação

Utilize o link enviado por e-mail para criar um repositório para seu grupo.
Cada membro do grupo deve clicar no link e selecionar o nome do grupo criado na
prática passada.
Não se esqueça de sair de sua conta **no github.com e no
classroom.github.com**.

**Crie um arquivo** chamado `alunos.txt` com os **nomes completos** de todos os
integrantes do grupo. Inclua também a **qual turma** pertencem.

## Avaliação das práticas

Utilizaremos a lista abaixo para avaliar a solução entregue de cada prática.

- [ ] Mensagens de commit que explicam claramente a mudança que foi feita
  [total|parcial|zero] 0.5 pt
- [ ] Formatação do código apropriada.
  Ex: `espacamento = (maximo - minimo)/(N - 1)`,
  `indices = range(0, N, 1)`, `dado = dados[i + 1]` == BOM.
  `espacamento=(maximo-minimo)/ (N-1)`, `indices=range (0,N,1)`,
  `dado= dados [i+ 1]` == RUIM [total|parcial|zero] 0.5 pt
- [ ] Utilizar variáveis ao invés de colocar número "na mão".
  Ex: `for i in range(0, N):`, `A[k][N - 1]` == BOM.
  `for i in range(0, 39):`, `A[k][47]` == RUIM. [total|parcial|zero] 1 pt
- [ ] Código com comentários que explicam "por que" algo foi feito, não só
  "o que" foi feito [total|parcial|zero] 1 pt
- [ ] Nomes de variáveis descritivos. Ex: `temperatura`, `media_por_hora`,
  `linha`, `somatorio` == BOM. `a`, `var`, `meh`, `lista` == RUIM.
  [total|parcial|zero] 2 pt
- [ ] Código produz a solução correta (**exatamente** como especificado em
  "Resultado esperado") [total|parcial|zero] 5 pt
- [ ] Tarefa bônus [total|parcial|zero] 1 pt extra (não será considerado
  caso a nota já seja 10)

Cada critério de avaliação poderá receber pontuação:

* Total: se atender **perfeitamente** ao critério
* Parcial: (metade da nota) se atender parcialmente ao critério
* Zero: se falhar ao critério

Note que a nota máxima, incluindo a tarefa bônus, é 10.
Cada grupo terá acesso a correção de sua solução.

## Entrega das soluções

A solução de cada prática será um repositório no [Github](http://github.com/)
com o código feito pelos alunos (criado a partir dos templates no
"Cronograma").
A entrega das soluções será feita criando uma
[Issue](https://guides.github.com/features/issues/)
no repositório da disciplina
[leouieda/matematica-especial](https://github.com/leouieda/matematica-especial/).
Utilize o link abaixo para ir direto para as Issues:

https://github.com/leouieda/matematica-especial/issues

Cada grupo deve criar uma Issue para entragar cada prática.
A issue deverá seguir o padrão abaixo:

* Título: Deve conter o nome da prática seguido dos nomes dos integrantes do
  grupo e a qual turma pertecem (caso haja mais de uma). Ex: "Prática
  Integração: Bilbo, John, Arthur - Turma 1"
* Corpo: Deve conter o link para o repositório do grupo (ex:
  `https://github.com/mat-esp-uerj/integracao-sociedade-42`) e qualquer
  comentário que achar necessário (ex: problemas com os commits, erros que foram
  arrumados depois, dificuldades, etc).

## License

All content can be freely used and adapted under the terms of the
[Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)
