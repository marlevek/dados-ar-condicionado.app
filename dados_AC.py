import streamlit as st

st.set_page_config('Informações para instalação ar-condicionado', page_icon=':mechanic:')
st.title('Dados Ar-Condicionado :material/heat_pump:')

parametros = {
'Agratto': {
        '9.000 a 12.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 20,  # g/m
                'limite_fabrica': 5.0,  # metros sem adicionar gás
                'limite_minimo': 2.0,   # mínima tubulação
                'limite_maximo': 15.0,  # máxima tubulação
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'evaporadora',
                'tubulacao': '1/4 e 3/8'
            }
        },   
        '18.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 20,  
                'limite_fabrica': 5.0,  
                'limite_minimo': 2.0,   
                'limite_maximo': 15.0,  
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'evaporadora',
                'tubulacao': '1/4 e 3/8'
            }
        },
        '24.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 20,  
                'limite_fabrica': 5.0,  
                'limite_minimo': 2.0,   
                'limite_maximo': 15.0,  
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 1/2'
            }
        },
        '30.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 20,  
                'limite_fabrica': 5.0,  
                'limite_minimo': 2.0,   
                'limite_maximo': 15.0,  
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 5/8'
            }
        },
},

'Daikin': {
        '9.000 a 12.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 20,  
                'limite_fabrica': 10.0,  
                'limite_minimo': 3.0,   
                'limite_maximo': 15.0,  
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 3/8'
            }
        }, 
        '18.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 0,
                'limite_fabrica': 15.0,
                'limite_minimo': 3.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 1/2'
            }
        },
        '24.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 20,
                'limite_fabrica': 10.0,
                'limite_minimo': 3.0,
                'limite_maximo': 30.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 1/2'
            }
        },
},
'Electrolux': {
        '9 a 12.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 12,
                'limite_fabrica': 8.0,
                'limite_minimo': 2.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 1/2'         
            }
        },
        '18.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 12,
                'limite_fabrica': 8.0,
                'limite_minimo': 2.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 1/2'       
                }
        },        
        '24.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 12,
                'limite_fabrica': 8.0,
                'limite_minimo': 2.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 1/2'       
            }
        }              
          
},
'Elgin': {
        '9 a 12.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 15,
                'limite_fabrica': 5.0,
                'limite_minimo': 3.5,
                'limite_maximo': 9.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 3/8'           
      }
  },
        '18.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 15,
                'limite_fabrica': 5.0,
                'limite_minimo': 3.5,
                'limite_maximo': 12.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 1/2'           
      }
  },
  
        '24.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 15,
                'limite_fabrica': 5.0,
                'limite_minimo': 4.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 5/8'           
      }
  },
        '30.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 15,
                'limite_fabrica': 5.0,
                'limite_minimo': 4.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 5/8'           
      }
  },
        '36.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 15,
                'limite_fabrica': 5.0,
                'limite_minimo': 4.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '3/8 e 5/8'           
      }
  },
},

'Fujitsu Airstage':{
        '9 a 12.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 20,
                'limite_fabrica': 5.0,
                'limite_minimo': 3.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 3/8'              
         }
     },
        '18.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 20,
                'limite_fabrica': 5.0,
                'limite_minimo': 3.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 1/2'              
         }
     },
        '24.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 30,
                'limite_fabrica': 5.0,
                'limite_minimo': 3.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 5/8'              
         }
     },
        '30 a 36.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 40,
                'limite_fabrica': 5.0,
                'limite_minimo': 3.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '3/8 e 5/8'              
         }
     },
 },
 
 'Gree': {
        '9 a 12.000 BTU/h': {
            'R-32':{
                'carga_por_metro': 15,
                'limite_fabrica': 5.0,
                'limite_minimo': 3.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/48 e 3/8'       
        }
    },
 },
 
'LG': {
        '9 a 15.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 20,
                'limite_fabrica': 7.5,
                'limite_minimo': 3.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 3/8'             
         }
     },
        '19.000 BTU/h': {
            'R-32':{
                'carga_por_metro': 20,
                'limite_fabrica': 7.5,
                'limite_minimo': 3.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 1/2'       
        }
    },
        '22.000 BTU/h': {
            'R-32':{
                'carga_por_metro': 20,
                'limite_fabrica': 7.5,
                'limite_minimo': 3.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 5/8'       
        }
    },
        '28 a 32.000 BTU/h': {
            'R-32':{
                'carga_por_metro': 20,
                'limite_fabrica': 7.5,
                'limite_minimo': 3.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '3/8 e 5/8'       
        }
    }     
 },
 
'Midea':{
   '9 a 12.000 BTU/h': {
       'R-32': {
            'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 25.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8'     
       }
   },
   '18.000 BTU/h': {
       'R-32': {
            'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 30.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8'     
       }
   },
   '24.000 BTU/h': {
       'R-32': {
            'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 30.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8'     
       }
   },
 },

'Samsung': {
    '9 a 12.000 BTU/h': {
        'R-32':{
            'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 15.0,
            'cabo_pp': '5 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8'       
      }
      },
  
    '18.000 BTU/h':{
        'R-32':{
            'carga_por_metro':15,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 15.0,
            'cabo_pp': '5 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 1/2'
    }  
  },
    '22.000 BTU/h':{
        'R-32':{
            'carga_por_metro':15,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 15.0,
            'cabo_pp': '5 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 5/8'
    }  
  },  
},

'TCL':{
    '9 a 12.000 BTU/h':{
        'R-32':{
            'carga_por_metro': 15.0,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8'
            }
    },
    '18.000 BTU/h':{
        'R-32':{
            'carga_por_metro': 25.0,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8'
            }
    },
    
    '24.000 BTU/h':{
        'R-32':{
            'carga_por_metro': 25.0,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 1/2'
            }
    },      
  }
}

fabricante = st.selectbox('**Fabricante**', list(parametros.keys()))
capacidades = list(parametros[fabricante].keys())
capacidade = st.selectbox('**Capacidade**', capacidades)
tipo_gas = st.selectbox('**Fluido Refrigerante**', ['R-32', 'R-410A', 'R-22'])
metros_tubulacao = st.number_input('**Digite o comprimento total da instalação**', min_value=0.0, step=0.5)


# Verificando se os parâmetros selecionados existem
dados = parametros.get(fabricante, {}).get(capacidade, {}).get(tipo_gas)

if dados:
    st.subheader(f"Informações para o aparelho de {capacidade} da marca {fabricante}")
    st.write(f"**Tubulação:** {dados['tubulacao']}")
    st.write(f"**Distância mínima:** {dados['limite_minimo']} metros")
    st.write(f"**Distância máxima:** {dados['limite_maximo']} metros")
    st.write(f"**Gás incluso para até:** {dados['limite_fabrica']} metros")
    st.write(f"**Cabo PP:** {dados['cabo_pp']}")
    st.write(f"**Ligação elétrica:** {dados['ligacao_eletrica']}")

    # Verificando se a distância da tubulação excede o limite máximo
    if metros_tubulacao > dados['limite_maximo']:
        st.warning("A distância da tubulação excede o limite máximo permitido.")
    elif metros_tubulacao > dados['limite_fabrica']:
        metros_excedentes = metros_tubulacao - dados['limite_fabrica']
        gas_adicional = metros_excedentes * dados['carga_por_metro']
        
        # Botão para adicionar gás
        if st.button('Adicionar Gás?'):
            st.success(f'Adicionar {gas_adicional} g de gás.')
    else:
        if st.button('Adicionar Gás?'):
            st.info('Não é necessário adicionar gás, pois a distância está dentro do limite.')
else:
    st.error("Configuração não encontrada. Verifique as opções selecionadas.")