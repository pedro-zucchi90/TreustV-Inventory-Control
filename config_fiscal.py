# Configurações e funções para cálculo fiscal do sistema de estoque
# Este arquivo centraliza as regras de negócio relacionadas a impostos, despesas e CMV (Custo das Mercadorias Vendidas)

# Taxa de impostos sobre vendas (ICMS + PIS/COFINS)
TAXA_IMPOSTOS_VENDAS = 0.18  # 18% de impostos aplicados sobre o valor total da venda

# Taxa de despesas administrativas (ex: custos de escritório, gestão, etc)
TAXA_DESPESAS_ADMINISTRATIVAS = 0.02  # 2% do valor da venda

# Taxa de despesas comerciais (ex: marketing, comissão, etc)
TAXA_DESPESAS_COMERCIAIS = 0.03  # 3% do valor da venda

# Função para calcular o valor total de impostos sobre uma venda
# Parâmetros:
#   valor_unitario: valor de venda de uma unidade do produto
#   quantidade: quantidade de unidades vendidas
# Retorna: valor total de impostos incidentes sobre a venda

def calcular_impostos_vendas(valor_unitario, quantidade):
    """Calcula impostos sobre vendas (ICMS + PIS/COFINS)"""
    return valor_unitario * quantidade * TAXA_IMPOSTOS_VENDAS

# Função para calcular o desconto aplicado em uma venda
# Parâmetros:
#   valor_unitario: valor de venda de uma unidade do produto
#   quantidade: quantidade de unidades vendidas
#   percentual_desconto: percentual de desconto informado pelo usuário (0-100)
# Retorna: valor total de desconto aplicado

def calcular_desconto_venda(valor_unitario, quantidade, percentual_desconto=None):
    """Calcula desconto sobre venda baseado SOMENTE no percentual informado pelo usuário"""
    valor_total = valor_unitario * quantidade
    if percentual_desconto is not None and percentual_desconto > 0:
        return valor_total * (percentual_desconto / 100)
    return 0.0

# Função para calcular despesas administrativas sobre uma venda
# Parâmetros:
#   valor_unitario: valor de venda de uma unidade do produto
#   quantidade: quantidade de unidades vendidas
# Retorna: valor total de despesas administrativas

def calcular_despesas_administrativas(valor_unitario, quantidade):
    """Calcula despesas administrativas da venda"""
    return valor_unitario * quantidade * TAXA_DESPESAS_ADMINISTRATIVAS

# Função para calcular despesas comerciais sobre uma venda
# Parâmetros:
#   valor_unitario: valor de venda de uma unidade do produto
#   quantidade: quantidade de unidades vendidas
# Retorna: valor total de despesas comerciais

def calcular_despesas_comerciais(valor_unitario, quantidade):
    """Calcula despesas comerciais da venda"""
    return valor_unitario * quantidade * TAXA_DESPESAS_COMERCIAIS

# Função para calcular o CMV (Custo das Mercadorias Vendidas)
# Parâmetros:
#   custo_unitario: custo de aquisição de uma unidade do produto
#   quantidade: quantidade de unidades vendidas
# Retorna: valor total do CMV

def calcular_cmv(custo_unitario, quantidade):
    """Calcula CMV (Custo das Mercadorias Vendidas)"""
    return custo_unitario * quantidade if custo_unitario else 0.0 