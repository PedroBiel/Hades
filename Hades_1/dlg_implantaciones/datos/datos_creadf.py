# -*- coding: utf-8 -*-
"""
Datos para crear el DataFrame para las implantaciones

Created on Fri Nov 20 14:23:35 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from dlg_implantaciones.datos.datos_relaciones import AplicaRelaciones


class CreaDF:
    """
    Aplica las relaciones en el DataFrame para las implantaciones.
    
    1. Reordena las columnas y renombra las columnas de las reacciones.
    2. Multiplica las reacciones por los signos (cargas de implantación).
    3. Divide las cargas por el número de ruedas.
    4. Mayora las cargas por el coeficiente de mayoración.
    5. Redondea las cargas.
    """
    
    def __init__(self):
        
        pass

    def reordena_columnas(self, df):
        """
        Reordena las columnas del DataFrame df y renombra las columnas de
        las reacciones.
        
        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con los datos de las implantaciones.
        """
        
        relaciones = AplicaRelaciones(df)
        df = relaciones.reordena_columnas()
        
        return df
        
    def multiplica_signos(self, df):
        """
        Multiplica las reacciones por los signos (cargas de implantación).
        
        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con los datos de las implantaciones.
        """
        
        relaciones = AplicaRelaciones(df)
        df = relaciones.multiplica_signos()
        
        return df
    
    def divide_ruedas(self, df):
        """
        Divide las cargas por el número de ruedas.
        
        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con los datos de las implantaciones.
        """
        
        relaciones = AplicaRelaciones(df)
        df = relaciones.divide_ruedas()
        
        return df
    
    def mayora_cargas(self, df):
        """
        Mayora las cargas por el coeficiente de mayoración.

        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con los datos de las implantaciones.
        """
        
        relaciones = AplicaRelaciones(df)
        df = relaciones.mayora_cargas()
        
        return df
    
    def redondea_cargas(self, df):
        """
        Redondea las cargas por el coeficiente de redondeo.

        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con los datos de las implantaciones.
        """
        
        relaciones = AplicaRelaciones(df)
        df = relaciones.redondea_cargas()
        
        return df
        
if __name__ == '__main__':
    
    import pandas as pd
    import random
    import string
    
    def gen_df():
        """Genera df aleatorio."""
        
        n_modelos = random.randint(1, 5)  # De 1 a 5 modelos.
        modelos = []
        for n in range(1, n_modelos + 1):
            modelos.append('modelo' + str(n))
        
        n_nudos = random.randint(1, 5)  # De 1 a 4 nudos.
        nudos = []
        apoyos = []
        ruedas = []
        for n in range(1, n_nudos + 1):
            nudos.append(n)
            apoyos.append('P' + str(n))
            ruedas.append(random.randint(1, 6))
        
        n_casos = random.randint(1, 10)  # De 1 a 4 nudos.
        casos = []
        grupos = []
        relaciones = []
        mayoraciones = []
        redondeos = []
        for n in range(1, n_casos + 1):
            casos.append(n)
            grupos.append(random.choice(string.ascii_uppercase))
            relaciones.append(random.choice(['Y', 'YO', 'O']))
            mayoraciones.append(random.choice([1.2, 1.1, 1.0]))
            redondeos.append(random.choice([5, 10, 50]))
    
        modelos_ = []
        nudos_ = []
        casos_ = []
        grupos_ = []
        relaciones_ = []
        mayoraciones_ = []
        redondeos_ = []
        apoyos_ = []
        ruedas_ = []
        Fx_ = []
        Fy_ = []
        Fz_ = []
        Mx_ = []
        My_ = []
        Mz_ = []
        
        for caso, grupo, relacion, mayoracion, redondeo in zip(
                casos, grupos, relaciones, mayoraciones, redondeos
                ):
            for nudo, apoyo, rueda in zip(nudos, apoyos, ruedas):
                for modelo in modelos:
                    modelos_.append(modelo)
                    nudos_.append(nudo)
                    casos_.append(caso)
                    grupos_.append(grupo)
                    relaciones_.append(relacion)
                    mayoraciones_.append(mayoracion)
                    redondeos_.append(redondeo)
                    apoyos_.append(apoyo)
                    ruedas_.append(rueda)
                    Fx_.append(random.randint(-500, 500))
                    Fy_.append(random.randint(-500, 500))
                    Fz_.append(random.randint(-1000, 1000))
                    Mx_.append(random.randint(-50, 50))
                    My_.append(random.randint(-100, 100))
                    Mz_.append(random.randint(-100, 100))
    
        d = {}
        d['Modelo'] = modelos_
        d['Nudo'] = nudos_
        d['Caso'] = casos_
        d['Grupo'] = grupos_
        d['Relación'] = relaciones_
        d['Mayoración'] = mayoraciones_
        d['Redondeo'] = redondeos_
        d['Apoyo'] = apoyos_
        d['Ruedas'] = ruedas_
        d['Fx'] = Fx_
        d['Fy'] = Fy_
        d['Fz'] = Fz_
        d['Mx'] = Mx_
        d['My'] = My_
        d['Mz'] = Mz_
        
        df = pd.DataFrame(d)
        df['signo_Fx'] = random.choice([-1, 0, 1])
        df['signo_Fy'] = random.choice([-1, 0, 1])
        df['signo_Fz'] = random.choice([-1, 0, 1])
        df['signo_Mx'] = random.choice([-1, 0, 1])
        df['signo_My'] = random.choice([-1, 0, 1])
        df['signo_Mz'] = random.choice([-1, 0, 1])
        
        return df
    
    def test_CreaDF(dCreaDF, num_steps):
        """
        Test de la clase CreaDF.
        
        dCreaDF : classe CreaDF
        num_steps : tupla de ints ; número de pruebas
        """
        print('COMIENZO DE LA PRUEBA')
        print('=====================')
        
        for steps in num_steps:
            print('STEPS :', steps)
            print('-------')
            for step in range(steps):
                print('STEP :', step)
                print('------')
                
                df = gen_df()
                print('\nDataFrame inicial')
                print(df)
                
                crea_df = dCreaDF()
                df = crea_df.reordena_columnas(df)
                df = crea_df.multiplica_signos(df)
                df = crea_df.divide_ruedas(df)
                df = crea_df.mayora_cargas(df)
                df = crea_df.redondea_cargas(df)
                print('\nDataFrame final')
                print(df)
                print('\n- - - - - - - - - - - - - - - - - - - -\n')
        
        print('FIN DE LA PRUEBA')
        print('================')
            
    test_CreaDF(CreaDF, (1, 10, 100, 1000, 10000))
        




        