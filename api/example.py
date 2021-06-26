import requests
from bs4 import BeautifulSoup
import json


class anime():
    def search_animes(name):
        # gogoanime2.org/search/ : (alt.)
        response_html = requests.get(
            f'https://www.gogoanime.ai/search.html?keyword={name}').text
        soup = BeautifulSoup(response_html, 'html.parser')
        items = soup.find('ul', {'class': 'items'}).find_all('li')
        results = []
        for i in items:
            result = {
                'title': i.a['title'],
                'anime-id': i.a['href'][10:],
                'image': ''+i.img['src']
            }
            results.append(result)
            # returns a json string
        return json.dumps(results)

    def anime_details(animeid):
        try:
            animelink = 'https://gogoanime.ai/category/{}'.format(animeid)
            response = requests.get(animelink)
            plainText = response.text
            soup = BeautifulSoup(plainText, "html.parser")
            source_url = soup.find("div", {"class": "anime_info_body_bg"}).img
            imgg = source_url.get('src')
            tit_url = soup.find(
                "div", {"class": "anime_info_body_bg"}).h1.string
            lis = soup.find_all('p', {"class": "type"})
            plot_sum = lis[1]
            pl = plot_sum.get_text().split(':')
            pl.remove(pl[0])
            sum = ""
            plot_summary = sum.join(pl)
            type_of_show = lis[0].a['title']
            ai = lis[2].find_all('a')  # .find_all('title')
            genres = []
            for link in ai:
                genres.append(link.get('title'))
            year1 = lis[3].get_text()
            year2 = year1.split(" ")
            year = year2[1]
            status = lis[4].a.get_text()
            oth_names = lis[5].get_text()
            lnk = soup.find(id="episode_page")
            ep_str = str(lnk.contents[-2])
            a_tag = ep_str.split("\n")[-2]
            a_tag_sliced = a_tag[:-4].split(">")
            last_ep_range = a_tag_sliced[-1]
            y = last_ep_range.split("-")
            ep_num = y[-1]
            res_detail_search = {"title": f"{tit_url}", "year": f"{year}", "other_names": f"{oth_names}", "type": f"{type_of_show}",
                                 "status": f"{status}", "genre": f"{genres}", "episodes": f"{ep_num}", "image_url": f"{imgg}", "plot_summary": f"{plot_summary}"}
            return res_detail_search
        except:
            pass

    def stream_anime(animeid, episode):
        BASE_URL = f'https://gogoanime.ai/{animeid}-episode-{episode}'
        RESULT_DICT = {'anime-id': f'{animeid}', 'episode': f'{episode}'}
        response = requests.get(BASE_URL)
        if (response.status_code == 200):
            soup = BeautifulSoup(response.text, 'html.parser')
            Ep_not_exist = soup.find('h1', {'class': 'entry-title'})
            if (Ep_not_exist is None):
                RESULT_DICT.update({'episode_exists': 'true'})
                div = soup.find('div', {'class': 'anime_muti_link'}).find('ul')
                div_li = div.find_all('li')
                for i in div_li:
                    RESULT_DICT.update(
                        {f"{i['class'][0]}": f"{i.a['data-video']}"})
                return RESULT_DICT
            else:
                return {'episode_exists': 'false'}
