from urllib.request import urlopen
from bs4 import BeautifulSoup as bS
import json
import re


def get_links(page):
    return page

def get_department_name(html):
    holder = html.find('div', {'id': 'content'})
    return holder.find('h1').text


def clean_course_description(data):
    data = data.replace("\n", "")
    pre_req = "None Listed"
    hours = "None Listed"
    recommendation = "None Listed"
    result1 = re.search('Prerequisites:(.*)Credit Hours', data)
    result2 = re.search('Hours:(.*)Prerequisites', data)
    if result1 is not None:
        pre_req = result1.group(1)
        pre_req = pre_req.replace("Prerequisites: ", "")
        hours = data.find('Credit Hours:')
        # pre_req = "Prerequisites:"+ pre_req
        if hours != -1:
            hours = data[hours:]
            hours = hours.replace("Credit Hours", "")
            stoping_point = data.find('Prerequisites:')
            data = data[0:stoping_point]

    if result2 is not None:
        hours = result2.group(1)
        hours = hours.replace(" ", "")
        pre_req = data.find('Prerequisites:')
        if pre_req != -1:
            pre_req = data[pre_req:]
            pre_req = pre_req.replace('Prerequisites: ', "")
            data = data[: data.find('Credit Hours:')]

    edge_case1 = re.search('Hours: (.*)Recommended', data)
    edge_case2 = re.search('Prerequisites:(.*)Credit Hour', data)
    edge_case3 = re.search('Hour:(.*)Prerequisites', data)

    if edge_case1 is not None:
        hours = edge_case1.group(1)
        check = data.find('Recommended:')
        if check != -1:
            recommendation = data[check+13:]
            data = data[0:check]

    if edge_case2 is not None:
        pre_req = edge_case2.group(1)
        check = data.find('Credit Hour:')
        # pre_req = "Prerequisites:" + pre_req
        if check != -1:
            hours = data[check:]
            hours = hours.replace('Credit Hour: ', '')
            stoping_point = data.find('Prerequisites:')
            data = data[0: stoping_point]

    if edge_case3 is not None:
        hours = edge_case3.group(1)
        hours = hours.replace(" ", "")
        check = data.find('Prerequisites:')
        if check != -1:
            pre_req = data[check:]
            pre_req = pre_req.replace("Prerequisites: ", "")
            # print(pre_req)
            data = data[: data.find('Credit Hour:')]
        else:
            pre_req = "None Listed"

    edge_case4 = data.find('Credit Hour:')
    if edge_case4 != -1:
        hours = data[edge_case4:]
        hours = hours.replace("Credit Hour: ", "")
        data = data[0:edge_case4]
        pre_req = "None Listed"

    if isinstance(pre_req, int) == False:
        edge_case5 = pre_req.find("Recommended: ")

        if edge_case5 != -1:
            recommendation = pre_req[edge_case5+13:]
            pre_req = pre_req[: edge_case5]
    edge_case4 = data.find('Credit Hours:')
    if edge_case4 != -1:
        hours = data[edge_case4:]
        hours = hours.replace("Credit Hours: ", "")

        data = data[0:edge_case4]

    if hours == -1:
        hours = 'None Listed'
    if pre_req == -1:
        pre_req = 'None Listed'

    if recommendation == -1:
        recommendation= 'None Listed'

    return data, hours, pre_req.replace('\xa0', ' '), recommendation.replace('\xa0', ' ')


if __name__ == "__main__":
    departments_list = ['ACCTCY', 'AERO', 'AG_EC', 'AG_ED_LD', 'AG_S_M', 'AFNR', 'ANESTH', 'AN_SCI', 'ANTHRO', 'ARABIC',
                        'ARCHST', 'AR_H_A', 'ART_CERM', 'ART_DRAW', 'ART_FIBR', 'ART_GNRL', 'ART_GRDN', 'ART_PNT',
                        'ART_PHOT', 'ART_PRNT', 'ART_SCUL', 'ASTRON', 'ATHTRN', 'ATM_SC', 'BIOCHM', 'BIOL_EN', 'BIO_SC',
                        'BIOMED', 'BL_STU', 'BUS_AD', 'CH_ENG', 'CHEM', 'CH_HTH', 'CHINSE', 'CV_ENG', 'CL_HUM', 'CLASS',
                        'CDS', 'CL_L_S', 'COMMUN', 'C_S_D', 'CMP_SC', 'DATA_SCI', 'DERM', 'DMU', 'DST', 'ECONOM',
                        'EDUC_H', 'ED_LPA', 'ESC_PS', 'ECE', 'EMR_ME', 'ENGINR', 'ENGLSH', 'ELSP', 'ENV_SC', 'ENV_ST',
                        'F_C_MD', 'FILM_S', 'FINANC', 'F_W', 'F_S', 'FOREST', 'FRENCH', 'GN_HES', 'G_STDY', 'GEOG',
                        'GEOL', 'GERMAN', 'GRAD', 'IEPG', 'GREEK', 'HMI', 'HTH_PR', 'HLTHPSYC', 'HLTH_SCI', 'HEBREW',
                        'HIST', 'GN_HON', 'HSP_MGMT', 'H_D_FS', 'IMSE', 'IS_LT', 'INFOTC', 'NEUROSCI', 'INTDSC',
                        'IN_MED', 'INTL_S', 'ITAL', 'JAPNSE', 'JOURN', 'KOREAN', 'LAB_AN', 'LATIN', 'LAW', 'LTC',
                        'LTC_V', 'LINGST', 'IEPL', 'MANGMT', 'MRKTNG', 'MATH', 'MAE', 'MPP', 'MED_ID', 'MDVL_REN',
                        'MICROB', 'MIL_SC', 'INFOINST', 'MUS_APMS', 'MUSIC_NM', 'MUS_ENS', 'MUS_GENL', 'MUS_I_VR',
                        'MUS_I_VT', 'MUS_EDUC', 'MUS_H_LI', 'MUS_THRY', 'NAT_R', 'NAVY', 'NEUROL', 'NU_ENG', 'NUCMED',
                        'NURSE', 'NUTRIT', 'NEP', 'OB_GYN', 'OC_THR', 'OPHTH', 'P_R_TR', 'PTH_AS', 'PEA_ST', 'FINPLN',
                        'PHIL', 'PM_REH', 'PH_THR', 'PHYSCS', 'PLNT_S', 'POL_SC', 'PORT', 'PSCHTY', 'PSYCH', 'PUB_AF',
                        'P_HLTH', 'RA_SCI', 'RADIOL', 'IEPR', 'REL_ST', 'RS_THR', 'RM_LAN', 'RU_SOC', 'RUSS',
                        'SCI_AG_J', 'SRV_LRN', 'SOC_WK', 'SOCIOL', 'SOIL', 'S_A_ST', 'SPAN', 'SPC_ED', 'IEPS', 'STAT',
                        'SSC', 'SURGRY', 'T_A_M', 'THEATR', 'V_BSCI', 'VMED_I', 'V_M_S', 'V_PBIO', 'WGST', 'IEPW'
                        ]


    all_offerings = urlopen('http://catalog.missouri.edu/courseofferings/')
    all_data = bS(all_offerings, 'html.parser')

    link_container = all_data.find('div', {'id': 'co_departments'})
    department_links = link_container.find_all('a', href=True)
    #print(department_links)
    department_complete_data = {}
    class_list = []
    for link in department_links:

        page = urlopen("http://catalog.missouri.edu/"+link['href'])

        page_data = bS(page, 'html.parser')

        department_name = get_department_name(page_data)
        print(department_name)
        department_info = department_name.split(' (')
        if len(department_info) == 2:
            department_name = department_info[0]
            department_code = department_info[1].replace(')', '')
        else:
            department_name = department_info[0] + ' ' + department_info[1].replace(')', '')
            department_code = department_info[2].replace(')', '')

        department_complete_data.update({
                        'department_name' : department_name,
                        'department_code' : department_code
        })

        # class_list.append('department_name: ' + department_name)

        courses = page_data.find('div', {'class': 'courses'})

        course_blocks = courses.find_all('div', {'class': 'courseblock'})

        for info in course_blocks:
            # Getting all the course numbers and titles

            class_name = info.find('p', {'class': 'courseblocktitle'}).text
            class_name = class_name.split(':  ')
            class_name[0] = class_name[0].replace("\xa0", " ")
            code, number = class_name[0].split(' ')
            number = number.replace("_", "")
            class_name[0] = number


            connections = []
            direct_connection_data = []
            class_description = info.find('p', {'class': 'courseblockdesc'}).text
            class_description = clean_course_description(class_description)

            for code in departments_list:
                points = [m.start() for m in re.finditer(r'(?={})'.format(re.escape(code)), class_description[2])]
                if len(points) > 0:
                    connections.append([len(code), points])

            # Check if there are any courses connected with the current course
            if len(connections) > 0:
                for data in connections:
                    word_len = int(data[0])
                    for info in data[1]:
                        start = int(info)
                        direct_connection_data.append(class_description[2][start: start + word_len + 5])

            # If there a no other class with a connection to the current one then mark it down as none listed
            if len(direct_connection_data) == 0:
                direct_connection_data = "None Listed"

            class_list.append(
                {
                    "name": class_name[1],
                    "number": class_name[0].replace('_', ''),
                    "description": class_description[0],
                    "prerequisites": class_description[2],
                    "hours": class_description[1],
                    "recommendation": class_description[3],
                    "connections" : direct_connection_data
                }
            )
        department_complete_data.update({"courses" : class_list})
        with open("../Output/"+department_code+".json", "w+") as outfile:
            outfile.write(json.dumps(department_complete_data, indent=4, sort_keys=False, separators=(',', ': '), ensure_ascii=False))


        class_list = []
        department_complete_data = {}

