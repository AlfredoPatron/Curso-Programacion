import unittest
import Cambia_Texto

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = Cambia_Texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUEN DIA')


if __name__ == '__main__':
    unittest.main()
