# AcessaData-Health — Verificação agregada demonstrativa.
# Execute a partir da raiz do repositório de publicação.
a <- read.csv("dados_publicos/conciliacao_anual.csv")
t <- read.csv("dados_publicos/confronto_tabnet.csv")
cr2 <- read.csv("dados_publicos/apc_cr2.csv", stringsAsFactors=FALSE)

esperados <- c(18094,18409,18979,19085,19665,18960,19579,20234,20291,21072)
stopifnot(
    nrow(a) == 10,
    identical(as.integer(a$ano), 2015:2024),
    identical(as.integer(a$total), as.integer(esperados)),
    all(a$total - a$classificados == a$diferenca),
    sum(a$total) == 194368,
    sum(a$classificados) == 194349,
    sum(a$diferenca) == 19,
    a$diferenca[a$ano == 2022] == 5,
    nrow(t) == 2,
    identical(as.integer(t$ano), c(2022L, 2023L)),
    all(t$sim_local == t$tabnet),
    all(t$diferenca == 0),
    all(t$sim_local == a$total[match(t$ano, a$ano)]),
    nrow(cr2) == 4,
    all(is.finite(cr2$apc)),
    all(cr2$ic_inferior < cr2$apc),
    all(cr2$apc < cr2$ic_superior),
    all(cr2$gl_satterthwaite > 0)
)
cat("APROVADO: conciliacao anual 2015-2024\n")
cat("APROVADO: confronto TabNet 2022-2023\n")
cat("APROVADO: estrutura dos quatro resultados CR2 transcritos\n")
cat("ESCOPO: verificacao de tabelas publicas agregadas, sem reprocessar microdados.\n")
