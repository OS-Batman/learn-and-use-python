import requests
from lxml import etree
import re
import json
import subprocess
import pprint

if __name__=="__main__":
    url='https://www.bilibili.com/video/BV1FV411d7u7?spm_id_from=333.337.search-card.all.click&vd_source=2d71be2fd8488770109d54c3a3ebe600'
    resp = requests.get(url)
    html=resp.text
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
        'Referer': url
    }
    # print(html)
    json_data = re.findall('<script>window.__playinfo__=(.*?)</script>',resp.text)[0]
    json_data = json.loads(json_data)
    # pprint.pprint(json_data)
    tree2 = etree.HTML(html)
    title = tree2.xpath('/html/body/div[2]/div[4]/div[1]/div[1]/h1')[0]
    # print(title.text)
    audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
    video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
    video_list = [title, audio_url, video_url]

def video_load(video_list):
    r1= requests.get(url=video_list[1], headers=head)
    audio_data = r1.content
    with open(title.text + '(audio).mp3', mode='wb') as f:
        f.write(audio_data)
    print('音频下载完成')
    r2= requests.get(url=video_list[2], headers=head)
    video_data = r2.content
    with open(title.text + '(video).mp4', mode='wb') as f:
        f.write(video_data)
    print('视频下载完成')

def video_add_mp4(video_name):
    video = video_name+"(video).mp4"
    audio = video_name+"(audio).mp3"
    #ffmpeg -i F:\pycharm\pycharmproject\bilibili献给新一代的演讲《后浪》(video).mp4 -i F:\pycharm\pycharmproject\bilibili献给新一代的演讲《后浪》(audio).mp3 -c:v copy -c:a copy F:\pycharm\pycharmproject\output.mp4
    cmd=f'ffmpeg -i {video} -i {audio} -acodec copy -vcodec copy {video_name+".mp4"}'
    subprocess.call(cmd, shell=True)
    # print(cmd)
    print("合并完成")

video_load(video_list)
video_add_mp4(title.text)