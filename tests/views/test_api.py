from base64 import b64encode
import json

import mock

from tests.base import BaseTestCase
import xml.etree.cElementTree as ET


class TestViewAPiCase(BaseTestCase):

    def setUp(self):
        # application.server.request.authorization = MagicMock(return_value=True)
        super(TestViewAPiCase, self).setUp()

    def load_fixtures(self):
        """
        Load the xml file
        """
        description = """
            <div class="foto componente_materia midia-largura-620">
                <img alt="Volkswagen Arteon (Foto: Divulgação)" height="413" id="209451" src="http://s2.glbimg.com/DIgFxpN0aAu99uvuZ3WmSqAUV2E=/620x413/e.glbimg.com/og/ed/f/original/2017/03/06/1_WKIn5xh.jpg" title="Volkswagen Arteon (Foto: Divulgação)" width="620" /><label class="foto-legenda">Volkswagen Arteon (Foto: Divulga&ccedil;&atilde;o)</label></div>
            <p>
                &nbsp;</p>
            <p>
                <strong>A <a href="http://revistaautoesporte.globo.com/carros/volkswagen">Volkswagen</a> revelou hoje (6) o Arteon, cup&ecirc; de quatro portas escolhido para suceder o CC</strong> &ndash; antes chamado Passat CC &ndash; e que ser&aacute; apresentado ao p&uacute;blico durante o Sal&atilde;o de Genebra. <strong>O visual n&atilde;o chega a ser novidade, j&aacute; que &eacute; praticamente o mesmo h&aacute; dois anos</strong>, <a href="http://revistaautoesporte.globo.com/Noticias/noticia/2015/03/volkswagen-sport-coupe-gte-adianta-visual-de-futuros-sedas.html">quando deu as caras no evento su&iacute;&ccedil;o como o prot&oacute;tipo Sport Coup&eacute; GTE Concept</a>.</p>
            <div class="foto componente_materia midia-largura-620">
                <img alt="Volkswagen Arteon (Foto: Divulgação)" height="413" id="209450" src="http://s2.glbimg.com/NgWcluzNZLlXwCu9Vs8N1UHXGbI=/620x413/e.glbimg.com/og/ed/f/original/2017/03/06/2_aEXyzmK.jpg" title="Volkswagen Arteon (Foto: Divulgação)" width="620" /><label class="foto-legenda">Volkswagen Arteon (Foto: Divulga&ccedil;&atilde;o)</label></div>
            <p>
                &nbsp;</p>
            <p>
                Para encarar o mundo real, a novidade recebeu ma&ccedil;anetas nas portas, antena no teto e alguns detalhes exigidos por lei... e s&oacute;! <strong>At&eacute; mesmo as rodas gigantes, os para-choques agressivos e a grade do motor integrada aos far&oacute;is continuam ali</strong> &ndash; para a alegria dos f&atilde;s. Al&eacute;m do pacote esportivo R-Line, tamb&eacute;m haver&aacute; op&ccedil;&otilde;es um pouco mais conservadoras.</p>
            <div class="foto componente_materia midia-largura-620">
                <img alt="Volkswagen Arteon (Foto: Divulgação)" height="413" id="209449" src="http://s2.glbimg.com/lJKzhfcrbXSzQZRKXCcn7pEIRjw=/620x413/e.glbimg.com/og/ed/f/original/2017/03/06/3_BZIDgsI.jpg" title="Volkswagen Arteon (Foto: Divulgação)" width="620" /><label class="foto-legenda">Volkswagen Arteon (Foto: Divulga&ccedil;&atilde;o)</label></div>
            <p>
                &nbsp;</p>
            <p>
                Se por fora tudo &eacute; diferente (e muito mais agressivo) comparado aos &ldquo;irm&atilde;os&rdquo;, o painel segue fiel ao estilo da marca &ndash; afinal, &eacute; o mesmo do Passat. N&atilde;o sabemos se a queda do teto compromete o espa&ccedil;o para a cabe&ccedil;a de quem vai atr&aacute;s, <strong>mas os 563 litros do porta-malas s&atilde;o bem aproveitados gra&ccedil;as &agrave; tampa traseira que abre com o vidro</strong>, como um hatch.</p>
            <div class="foto componente_materia midia-largura-620">
                <img alt="Volkswagen Arteon (Foto: Divulgação)" height="413" id="209447" src="http://s2.glbimg.com/RJ9LxS8YaH4bCAlP1f_1Nm8cocY=/620x413/e.glbimg.com/og/ed/f/original/2017/03/06/4_vYYIbul.jpg" title="Volkswagen Arteon (Foto: Divulgação)" width="620" /><label class="foto-legenda">Volkswagen Arteon (Foto: Divulga&ccedil;&atilde;o)</label></div>
            <p>
                &nbsp;</p>
            <p>
                A plataforma &eacute; a mesma MQB utilizada no Passat (que, gra&ccedil;as ao milagre da modularidade, tamb&eacute;m serve ao Golf e, futuramente, &agrave; nova gera&ccedil;&atilde;o do Gol nacional). <strong>S&atilde;o 4,86 metros de comprimento; 1,87 m de largura; 1,42 m de altura; e 2,84 m de entre-eixos</strong>. Ainda que pare&ccedil;a um latif&uacute;ndio, apenas quatro ocupantes viajam com conforto na cabine.</p>
            <div class="foto componente_materia midia-largura-620">
                <img alt="Volkswagen Arteon (Foto: Divulgação)" height="413" id="209446" src="http://s2.glbimg.com/EDuoev-xcbKnAK_QVWRclJa4Mac=/620x413/e.glbimg.com/og/ed/f/original/2017/03/06/5_71gviOe.jpg" title="Volkswagen Arteon (Foto: Divulgação)" width="620" /><label class="foto-legenda">Volkswagen Arteon (Foto: Divulga&ccedil;&atilde;o)</label></div>
            <p>
                &nbsp;</p>
            <p>
                No Velho Continente, <strong>ser&atilde;o oferecidos motores a gasolina (1.5 turbo com 150 cv e 2.0 turbo nas op&ccedil;&otilde;es de 190 cv e 280 cv) e tamb&eacute;m a diesel (2.0 turbo nas op&ccedil;&otilde;es de 150 cv, 190 cv e 240 cv)</strong>. Com exce&ccedil;&atilde;o das vers&otilde;es de entrada, que t&ecirc;m c&acirc;mbio manual de seis marchas, a transmiss&atilde;o &eacute; sempre automatizada com dupla embreagem e sete marchas.</p>
            <div class="saibamais componente_materia expandido">
                <strong>saiba mais</strong>
                <ul>
                    <li>
                        <a href="http://revistaautoesporte.globo.com/Noticias/noticia/2016/01/os-12-mimos-mais-legais-do-volkswagen-passat.html">OS 12 MIMOS MAIS LEGAIS DO VOLKSWAGEN PASSAT</a></li>
                    <li>
                        <a href="http://revistaautoesporte.globo.com/Analises/noticia/2015/11/avaliacao-novo-volkswagen-passat.html">AVALIA&Ccedil;&Atilde;O: NOVO VOLKSWAGEN PASSAT</a></li>
                </ul>
            </div>
            <p>
                &nbsp;</p>
            <div class="foto componente_materia midia-largura-620">
                <img alt="Volkswagen Arteon (Foto: Divulgação)" height="413" id="209448" src="http://s2.glbimg.com/fkJMyLGJsX_ThzJBHalbemmcb4M=/620x413/e.glbimg.com/og/ed/f/original/2017/03/06/6_pih5QJE.jpg" title="Volkswagen Arteon (Foto: Divulgação)" width="620" /><label class="foto-legenda">Volkswagen Arteon (Foto: Divulga&ccedil;&atilde;o)</label></div>
            <p>
                &nbsp;</p>
        """

        channel = ET.Element("channel")
        item = ET.SubElement(channel, "item")

        ET.SubElement(item, "title").text = "Waze lançará serviço de caronas no Brasil ainda este ano"
        ET.SubElement(item, "description").text = description
        ET.SubElement(item, "link").text = "http://revistaautoesporte.globo.com/Noticias/noticia/2017/03/waze-lancara-servico-de-caronas-no-brasil-ainda-este-ano.html"

        tree = ET.ElementTree(channel)
        tree.write("feed.xml")

    @mock.patch('crawler.views.api.business.create_update_file_xml')
    @mock.patch('requests.get')
    def test_index_logged(self, mock_requests_get, mock_create_update_file_xml):
        headers = {
            'Authorization': 'Basic %s' % b64encode(b"admin:password").decode("ascii")
        }
        response = self.client.get("/api/", headers=headers)
        self.assertEqual(response.status_code, 200)
        r = json.loads(response.data.decode('utf-8'))
        self.assertEqual(r['feed'][0]['item']['title'], 'Waze lançará serviço de caronas no Brasil ainda este ano')
        self.assertEqual(r['feed'][0]['item']['link'], 'http://revistaautoesporte.globo.com/Noticias/noticia/2017/03/waze-lancara-servico-de-caronas-no-brasil-ainda-este-ano.html')
        self.assertEqual(r['feed'][0]['item']['description'][1]['type'], 'text')
        self.assertEqual(r['feed'][0]['item']['description'][1]['content'], 'A Volkswagen revelou hoje (6) o Arteon, cupê de quatro portas escolhido para suceder o CC – antes chamado Passat CC – e que será apresentado ao público durante o Salão de Genebra. O visual não chega a ser novidade, já que é praticamente o mesmo há dois anos, quando deu as caras no evento suíço como o protótipo Sport Coupé GTE Concept.')

    @mock.patch('crawler.views.api.business.create_update_file_xml')
    @mock.patch('requests.get')
    def test_index_not_logged(self, mock_requests_get, mock_create_update_file_xml):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 401)

