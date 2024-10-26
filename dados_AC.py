import streamlit as st

st.set_page_config('Informações para instalação ar-condicionado Hi Wall', page_icon=':mechanic:')
st.title('Características Ar-Condicionado Hi Wall :material/heat_pump:')

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
                'cabo_pp': '4 x 1,5mm (maioria); ou 5 x 1,5mm para os modelos UI/UE (quente e frio)',
                'ligacao_eletrica': 'Na condensadora para os modelos JI/JE (só frio e quente-frio), YI/YE (só frio e quente-frio) e UI/UE (só frio), e na Evaporadora para os modelos UI/UE (quente-frio)',
                'tubulacao': '1/4 e 3/8',

            }
        },
        '18.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 12,
                'limite_fabrica': 8.0,
                'limite_minimo': 2.0,
                'limite_maximo': 15.0,
               'cabo_pp': '4 x 1,5mm (maioria); ou 5 x 1,5mm para os modelos UI/UE (quente e frio)',
                'ligacao_eletrica': 'Na condensadora para os modelos JI/JE (só frio e quente-frio), YI/YE (só frio e quente-frio) e UI/UE (só frio), e na Evaporadora para os modelos UI/UE (quente-frio)',
                'tubulacao': '1/4 e 1/2',   
                }
        },        
        '24.000 BTU/h': {
            'R-32': {
                'carga_por_metro': 12,
                'limite_fabrica': 8.0,
                'limite_minimo': 2.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm (maioria); ou 5 x 1,5mm para os modelos UI/UE (quente e frio)',
                'ligacao_eletrica': 'Na condensadora para os modelos JI/JE (só frio e quente-frio), YI/YE (só frio e quente-frio) e UI/UE (só frio), e na Evaporadora para os modelos UI/UE (quente-frio)',
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
        '9.000 BTU/h': {
            'R-32':{
                'carga_por_metro': 12,
                'limite_fabrica': 5.0,
                'limite_minimo': 2.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 3/8',
                'observacoes': ('Se for modelo só frio, a carga adicional de gás é 12g/metro acima de 5m')    
        }
    },
        '12.000 BTU/h': {
            'R-32':{
                'carga_por_metro': 12,
                'limite_fabrica': 5.0,
                'limite_minimo': 2.0,
                'limite_maximo': 20.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 3/8',
                'observacoes': ('Se for modelo só frio, a carga adicional de gás é 12g/metro acima de 5m')       
        }
    },
        '18.000 BTU/h': {
            'R-32':{
                'carga_por_metro': 12,
                'limite_fabrica': 5.0,
                'limite_minimo': 2.0,
                'limite_maximo': 25.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 1/2',
                'observacoes': ('Se for modelo só frio, a carga adicional de gás é 12g/metro acima de 5m')       
        }
    },
        '24.000 BTU/h': {
            'R-32':{
                'carga_por_metro': 20,
                'limite_fabrica': 5.0,
                'limite_minimo': 2.0,
                'limite_maximo': 25.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 1/2'       
        }
    },
},
 
'Hitachi':{
        '9.000 BTU/h':{
            'R-32':{
                'carga_por_metro': 20,
                'limite_fabrica': 5,
                'limite_minimo': 3.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 3/8'
                }
        },
        '12.000 BTU/h':{
            'R-32':{
                'carga_por_metro': 20,
                'limite_fabrica': 5,
                'limite_minimo': 3.0,
                'limite_maximo': 15.0,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 3/8'
                }
        },
        '18.000 BTU/h':{
            'R-32':{
                'carga_por_metro': 20,
                'limite_fabrica': 5.0,
                'limite_minimo': 3.0,
                'limite_maximo':30.0 ,
                'cabo_pp': '4 x 1,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 1/2'
                }
        },
        '24.000 BTU/h':{
            'R-32':{
                'carga_por_metro': 20,
                'limite_fabrica': 5.0,
                'limite_minimo': 3.0,
                'limite_maximo': 30.0,
                'cabo_pp': '4 x 2,5mm',
                'ligacao_eletrica': 'condensadora',
                'tubulacao': '1/4 e 5/8'
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
   '9.000 BTU/h': {
       'R-32': {
            'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8'     
       }
   },
   '12.000 BTU/h': {
       'R-32': {
            'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 1/2'     
       }
   },
   '18.000 BTU/h': {
       'R-32': {
            'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
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
            'limite_minimo': 2.0,
            'limite_maximo': 30.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '3/8 e 5/8',
            'observacoes': ('Se o comprimento da tubulação for maior que 25m mudar tubulação da linha de sucção para 5/8')      
       }
   },
 },

'Philco':{
   '9.000 BTU/h': {
       'R-32': {
            'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8'     
       }
   },
   '12.000 BTU/h': {
       'R-32': {
            'carga_por_metro': 15,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8'     
       }
   },
   '18.000 BTU/h': {
       'R-32': {
            'carga_por_metro': 25,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 25.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8'    
       }
   },
   '24.000 BTU/h': {
       'R-32': {
            'carga_por_metro': 25,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 25.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 1/2',   
       }
   },
   '30.000 BTU/h': {
       'R-32': {
            'carga_por_metro': 25,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 25.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 1/2',   
       }
   },
   '36.000 BTU/h': {
       'R-32': {
            'carga_por_metro': 25,
            'limite_fabrica': 5.0,
            'limite_minimo': 2.0,
            'limite_maximo': 25.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 1/2',   
       }
   },   
 },

'Samsung': {
    '9 a 12.000 BTU/h': {
        'R-410a':{
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
        'R-410a':{
            'carga_por_metro':15,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 300,
            'cabo_pp': '5 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 1/2'
    }  
  },
    '22.000 BTU/h':{
        'R-410a':{
            'carga_por_metro':15,
            'limite_fabrica': 5.0,
            'limite_minimo': 3.0,
            'limite_maximo': 30.0,
            'cabo_pp': '5 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 5/8'
    }  
  },  
},

'TCL':{
    '9.000 BTU/h':{
        'R-410a':{
            'carga_por_metro': 15.0,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8'
            }
    },
    '12.000 BTU/h':{
        'R-32':{
            'carga_por_metro': 15.0,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8',
            },
         'R-410a':{
            'carga_por_metro': 20.0,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8',
            },  
    },
    '18.000 BTU/h':{
        'R-32':{
            'carga_por_metro': 25.0,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8',
            },       
        'R-410a':{
            'carga_por_metro': 30.0,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 3/8',
            },     
    },  
    '24.000 BTU/h':{
        'R-32':{
            'carga_por_metro': 25.0,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 1/2',
            },
        'R-410a':{
            'carga_por_metro': 30.0,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 1/2',
            },       
    }, 
    '32.000 BTU/h':{
        'R-410a':{
            'carga_por_metro': 30.0,
            'limite_fabrica': 3.0,
            'limite_minimo': 2.0,
            'limite_maximo': 15.0,
            'cabo_pp': '4 x 1,5mm',
            'ligacao_eletrica': 'condensadora',
            'tubulacao': '1/4 e 1/2',
            }
    },       
  },
}

fabricante = st.selectbox('**Fabricante**', list(parametros.keys()))
capacidades = list(parametros[fabricante].keys())
capacidade = st.selectbox('**Capacidade**', capacidades)
tipos_gas = list(parametros[fabricante][capacidade].keys())
tipo_gas = st.selectbox('**Fluido Refrigerante**', tipos_gas)
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

    # Exibir observações, se houver
    if 'observacoes' in dados:
        st.info(f'**Observações:** {dados['observacoes']}')
    
    # Verificando se a distância da tubulação excede o limite máximo
    if metros_tubulacao < dados['limite_minimo']:
        st.warning("O comprimento mínimo da tubulação é menor do que o permitido. Verifique a distância mínima.")
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