import requests
import base64
import re
import sys

# r =requests.get('https://tryhackme.com/badge/319961')
url = "https://tryhackme.com/badge/" + sys.argv[1]
r =requests.get(url)
text = r.text
start = text.find('(\"')
end = text.find('\")')
text = text[start+2:end]
text_plain = base64.b64decode(text).decode('utf-8')

reg_str_nickname = r"<span class=\"thm_nickname\">(.*?)</span>"
nickname = re.findall(reg_str_nickname,text_plain)[0]

reg_str_title = r"<span class=\"thm_rank\">(.*?)</span>"
title = re.findall(reg_str_title,text_plain)[0]

reg_str_rank = r"<span class=\"thm_stat thm_mr\">(.*?)</span>"
rank = re.findall(reg_str_rank,text_plain)

reg_str_badges = r"<span class=\"thm_stat\">(.*?)</span>"
badges = re.findall(reg_str_badges,text_plain)[0]

svg = "<svg        width=\"405\"        height=\"130\" viewBox=\"0 0 405 130\"        fill=\"none\"        xmlns=\"http://www.w3.org/2000/svg\"      >      	<style>          .header {            font: 800 18px 'Segoe UI', Ubuntu, Sans-Serif;            fill: #d71478;            animation: fadeInAnimation 0.8s ease-in-out forwards;          }          .title {      		opacity: 0;            font: 300 13px 'Segoe UI', Ubuntu, Sans-Serif;            fill: #6071C8;      		animation: fadeInAnimation 0.3s ease-in-out forwards;              }          .stats {      		opacity: 0;            font: 600 13px 'Segoe UI', Ubuntu, Sans-Serif;            fill: #88cc14;      		animation: fadeInAnimation 0.3s ease-in-out forwards;              }          .number {      		opacity: 0;            font: 600 13px 'Segoe UI', Ubuntu, Sans-Serif;            fill: #FFFFFF;      		animation: fadeInAnimation 0.3s ease-in-out forwards;              }          .trophy {      		opacity: 0;      		animation: fadeInAnimation 0.3s ease-in-out forwards;            animation-delay: 600ms;              }          .door {      		opacity: 0;      		animation: fadeInAnimation 0.3s ease-in-out forwards;            animation-delay: 750ms;              }          .award {      		opacity: 0;      		animation: fadeInAnimation 0.3s ease-in-out forwards;            animation-delay: 800ms;              }                              @keyframes fadeInAnimation {      		from {       		 opacity: 0;     			 }     		 to {     		   opacity: 1;      			}   			 }         </style>    <defs>    <filter id=\"f1\" x=\"0\" y=\"0\">      <feGaussianBlur in=\"SourceGraphic\" stdDeviation=\"3\" />    </filter>  </defs>        <rect          x=\"0\"          y=\"0\"          rx=\"4.5\"          ry=\"4.5\"          height=\"100%\"          stroke=\"#88cc14\"          width=\"100%\"          fill=\"#141321\"          stroke-opacity=\"1\"        />    <g        data-testid=\"card-title\"        transform=\"translate(25, 35)\"      >        <g transform=\"translate(0, 0)\">       <text        x=\"220\"        y=\"-10\"        text-anchor = \"middle\"        class=\"header\"        data-testid=\"header\"      >"+ nickname +"</text>    </g>      </g>	<g        data-testid=\"card-title\"        transform=\"translate(25, 35)\"      >        <g transform=\"translate(0, 0)\" filter= \"url(#f1)\">       <text        x=\"220\"        y=\"-10\"        text-anchor = \"middle\"        class=\"header\"        data-testid=\"header\"      >"+ nickname +"</text>    </g>      </g>     <g        data-testid=\"card-title\"        transform=\"translate(25, 35)\"      >        <g transform=\"translate(0, 0)\">      <text        x=\"220\"        y=\"6\"        text-anchor = \"middle\"        class=\"title\"        style=\"animation-delay: 450ms\"        data-testid=\"title\"      >"+ title +"</text>    </g>      </g>          <g        data-testid=\"card-title\"        transform=\"translate(25, 35)\"      >        <g transform=\"translate(0, 0)\">      <text        x=\"165\"        y=\"78\"        text-anchor = \"middle\"        class=\"number\"        style=\"animation-delay: 600ms\"        data-testid=\"number\"      >#"+rank[0]+"</text>    </g>      </g>      <g        data-testid=\"card-title\"        transform=\"translate(25, 35)\"      >        <g transform=\"translate(0, 0)\">      <text        x=\"165\"        y=\"65\"        text-anchor = \"middle\"        class=\"stats\"        style=\"animation-delay: 600ms\"        data-testid=\"stats\"      >RANK</text>    </g>      </g>            <g        data-testid=\"card-title\"        transform=\"translate(25, 35)\"      >        <g transform=\"translate(0, 0)\">      <text        x=\"230\"        y=\"78\"        text-anchor = \"middle\"        class=\"number\"        style=\"animation-delay: 750ms\"        data-testid=\"stats\"      >"+ rank[1] +"</text>    </g>      </g>      <g        data-testid=\"card-title\"        transform=\"translate(25, 35)\"      >        <g transform=\"translate(0, 0)\">      <text        x=\"230\"        y=\"65\"        text-anchor = \"middle\"        class=\"stats\"        style=\"animation-delay: 750ms\"        data-testid=\"stats\"      >ROOMS</text>    </g>      </g>            <g        data-testid=\"card-title\"        transform=\"translate(25, 35)\"      >        <g transform=\"translate(0, 0)\">      <text        x=\"290\"        y=\"78\"        text-anchor = \"middle\"        class=\"number\"        style=\"animation-delay: 900ms\"        data-testid=\"stats\"      >"+badges+"</text>    </g>      </g>      <g        data-testid=\"card-title\"        transform=\"translate(25, 35)\"      >        <g transform=\"translate(0, 0)\">      <text        x=\"290\"        y=\"65\"        text-anchor = \"middle\"        class=\"stats\"        style=\"animation-delay: 900ms\"        data-testid=\"stats\"      >BADGES</text>    </g>      </g><svg xmlns=\"http://www.w3.org/2000/svg\" x=\"175\" y=\"55\" width=\"30\" height=\"30\" fill=\"#FFFFFF\" class=\"trophy\" viewBox=\"0 0 16 16\">  <path d=\"M2.5.5A.5.5 0 0 1 3 0h10a.5.5 0 0 1 .5.5c0 .538-.012 1.05-.034 1.536a3 3 0 1 1-1.133 5.89c-.79 1.865-1.878 2.777-2.833 3.011v2.173l1.425.356c.194.048.377.135.537.255L13.3 15.1a.5.5 0 0 1-.3.9H3a.5.5 0 0 1-.3-.9l1.838-1.379c.16-.12.343-.207.537-.255L6.5 13.11v-2.173c-.955-.234-2.043-1.146-2.833-3.012a3 3 0 1 1-1.132-5.89A33.076 33.076 0 0 1 2.5.5zm.099 2.54a2 2 0 0 0 .72 3.935c-.333-1.05-.588-2.346-.72-3.935zm10.083 3.935a2 2 0 0 0 .72-3.935c-.133 1.59-.388 2.885-.72 3.935z\"/></svg><svg xmlns=\"http://www.w3.org/2000/svg\" x= \"240\" y=\"55\" width=\"30\" height=\"30\" fill=\"#FFFFFF\" class=\"door\" viewBox=\"0 0 16 16\">  <path d=\"M1.5 15a.5.5 0 0 0 0 1h13a.5.5 0 0 0 0-1H13V2.5A1.5 1.5 0 0 0 11.5 1H11V.5a.5.5 0 0 0-.57-.495l-7 1A.5.5 0 0 0 3 1.5V15H1.5zM11 2h.5a.5.5 0 0 1 .5.5V15h-1V2zm-2.5 8c-.276 0-.5-.448-.5-1s.224-1 .5-1 .5.448.5 1-.224 1-.5 1z\"/></svg><svg xmlns=\"http://www.w3.org/2000/svg\" x=\"300\" y =\"55\" width=\"30\" height=\"30\" fill=\"#FFFFFF\" class=\"award\" viewBox=\"0 0 16 16\">  <path d=\"M9.669.864 8 0 6.331.864l-1.858.282-.842 1.68-1.337 1.32L2.6 6l-.306 1.854 1.337 1.32.842 1.68 1.858.282L8 12l1.669-.864 1.858-.282.842-1.68 1.337-1.32L13.4 6l.306-1.854-1.337-1.32-.842-1.68L9.669.864zm1.196 1.193.684 1.365 1.086 1.072L12.387 6l.248 1.506-1.086 1.072-.684 1.365-1.51.229L8 10.874l-1.355-.702-1.51-.229-.684-1.365-1.086-1.072L3.614 6l-.25-1.506 1.087-1.072.684-1.365 1.51-.229L8 1.126l1.356.702 1.509.229z\"/>  <path d=\"M4 11.794V16l4-1 4 1v-4.206l-2.018.306L8 13.126 6.018 12.1 4 11.794z\"/></svg><svg   xmlns:dc=\"http://purl.org/dc/elements/1.1/\"   xmlns:cc=\"http://creativecommons.org/ns#\"   xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"   xmlns:svg=\"http://www.w3.org/2000/svg\"   xmlns=\"http://www.w3.org/2000/svg\"   viewBox=\"-40 0 475 225\"   height=\"90\"   width=\"130\"   xml:space=\"preserve\"   id=\"svg2\"   version=\"1.1\"><metadata     id=\"metadata8\"><rdf:RDF><cc:Work         rdf:about=\"\"><dc:format>image/svg+xml</dc:format><dc:type           rdf:resource=\"http://purl.org/dc/dcmitype/StillImage\" /></cc:Work></rdf:RDF></metadata><defs     id=\"defs6\" /><g     transform=\"matrix(1.3333333,0,0,-1.3333333,0,246.66667)\"     id=\"g10\"><g       transform=\"scale(0.1)\"       id=\"g12\"><path         id=\"path14\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 2064.53,973.359 h -78.67 v 324.921 h -109.45 v 74.14 h 297.57 v -74.14 H 2064.53 V 973.359\" /><path         id=\"path16\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 2371.76,1192.27 c -53.01,0 -79.81,-35.9 -79.81,-90.08 V 973.359 h -72.38 V 1258.4 h 48.44 l 8.01,-61.56 c 21.09,39.92 59.25,65.54 112.85,65.54 h 11.99 v -70.11 h -29.1\" /><path         id=\"path18\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 2743.98,1009.84 c 0,-83.199 -54.14,-145.352 -142.5,-145.352 -52.46,0 -95.78,18.793 -126.56,44.461 l 41.06,43.903 c 27.34,-13.672 53,-22.813 85.5,-22.231 41.06,0 69.54,21.098 69.54,62.699 v 18.24 c -18.25,-23.361 -48.44,-33.63 -78.09,-33.63 -82.66,0 -124.84,56.45 -124.84,139.1 v 141.37 h 72.38 v -137.38 c 0,-52.47 25.08,-72.97 63.87,-72.97 41.01,0 67.26,24.53 67.26,79.25 v 131.1 h 72.38 v -248.56\" /><path         id=\"path20\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"M 2144.92,465.43 V 629.059 H 1990.43 V 465.43 h -78.67 v 399.058 h 78.67 V 703.16 h 154.49 v 161.328 h 78.67 V 465.43 h -78.67\" /><path         id=\"path22\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 2526.25,607.969 c 0,46.722 -35.94,76.371 -73.55,76.371 -38.17,0 -73.52,-29.649 -73.52,-76.371 0,-46.758 35.35,-75.821 73.52,-75.821 37.61,0 73.55,29.063 73.55,75.821 z m 18.24,-142.539 -3.98,40.468 c -21.1,-26.796 -55.31,-43.867 -94.65,-43.867 -80.94,0 -139.06,64.957 -139.06,145.938 0,80.941 58.12,146.48 139.06,146.48 39.34,0 73.55,-17.648 94.65,-44.449 l 3.98,40.469 h 48.48 V 465.43 h -48.48\" /><path         id=\"path24\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 2931.52,701.449 -43.32,-46.758 c -23.4,21.68 -43.9,29.098 -68.98,29.098 -38.2,0 -73.56,-29.098 -73.56,-75.82 0,-46.758 35.36,-75.821 73.56,-75.821 25.08,0 45.58,7.383 68.98,29.063 l 43.32,-46.762 c -26.79,-31.91 -67.26,-52.418 -112.3,-52.418 -80.98,0 -145.94,64.957 -145.94,145.938 0,80.941 64.96,145.941 145.94,145.941 45.04,0 85.51,-20.551 112.3,-52.461\" /><path         id=\"path26\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 3158.36,541.25 c -17.11,26.211 -26.8,35.941 -54.14,35.941 h -19.96 V 465.43 h -72.38 v 399.058 h 72.38 V 646.719 h 17.65 c 26.8,0 36.49,9.14 53.6,35.902 l 44.45,67.848 h 80.39 l -63.87,-96.328 c -11.95,-18.832 -27.93,-36.481 -40.43,-41.602 14.22,-4.57 30.2,-22.809 43.33,-42.769 l 68.39,-104.34 h -80.39 l -49.02,75.82\" /><path         id=\"path28\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"M 2224.73,7.80859 V 262.66 L 2104.45,113.281 1984.73,262.66 V 7.80859 h -78.68 V 406.879 h 46.76 l 151.64,-190.43 152.19,190.43 h 46.76 V 7.80859 h -78.67\" /><path   \
      id=\"path30\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 2472.07,175.98 h 130.55 c 0,6.829 -2.31,15.969 -6.84,22.809 -9.69,18.242 -30.23,31.91 -57.58,31.91 -38.79,0 -65,-27.34 -66.13,-54.719 z m 191.52,43.899 c 12,-26.207 12.54,-65 4.57,-89.488 h -198.94 c 0,-38.7894 31.91,-59.8793 70.66,-59.8793 29.65,0 60.43,6.8672 86.1,19.9571 l 38.2,-41.5977 C 2633.4,26.0508 2590.62,4.41016 2539.88,4.41016 c -86.64,0 -145.35,62.69924 -145.35,145.94184 0,80.937 54.73,146.488 143.67,146.488 60.98,0 103.75,-29.07 125.39,-76.961\" /><path         id=\"path32\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 976.051,894.77 v 135.19 l -34.289,-26.48 -22.621,30.93 60.55,44.46 h 39.799 v -184.1 h -43.439\" /><path         id=\"path34\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1154.41,987.34 c 0,5.711 -0.35,12.039 -1.01,18.99 -0.7,6.91 -1.99,13.4 -3.91,19.37 -1.91,5.98 -4.65,11.02 -8.2,15.08 -3.56,4.06 -8.17,6.1 -13.91,6.1 -5.7,0 -10.39,-2.04 -14.02,-6.1 -3.67,-4.06 -6.48,-9.1 -8.48,-15.08 -1.99,-5.97 -3.32,-12.46 -4.02,-19.37 -0.7,-6.951 -1.06,-13.279 -1.06,-18.99 0,-5.891 0.36,-12.34 1.06,-19.371 0.7,-7.028 2.03,-13.52 4.02,-19.489 2,-5.98 4.81,-11.019 8.48,-15.082 3.63,-4.097 8.32,-6.128 14.02,-6.128 5.74,0 10.35,2.031 13.91,6.128 3.55,4.063 6.29,9.102 8.2,15.082 1.92,5.969 3.21,12.461 3.91,19.489 0.66,7.031 1.01,13.48 1.01,19.371 z m 44.73,0 c 0,-13 -1.29,-25.391 -3.91,-37.18 -2.57,-11.801 -6.75,-22.148 -12.46,-31.058 -5.74,-8.942 -13.12,-16.051 -22.22,-21.332 -9.1,-5.27 -20.16,-7.93 -33.17,-7.93 -13,0 -24.1,2.66 -33.28,7.93 -9.18,5.281 -16.68,12.39 -22.5,21.332 -5.78,8.91 -10,19.257 -12.62,31.058 -2.57,11.789 -3.86,24.18 -3.86,37.18 0,13.01 1.29,25.36 3.86,37.04 2.62,11.71 6.84,21.95 12.62,30.7 5.82,8.75 13.32,15.7 22.5,20.94 9.18,5.19 20.28,7.77 33.28,7.77 13.01,0 24.07,-2.58 33.17,-7.77 9.1,-5.24 16.48,-12.19 22.22,-20.94 5.71,-8.75 9.89,-18.99 12.46,-30.7 2.62,-11.68 3.91,-24.03 3.91,-37.04\" /><path         id=\"path36\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1443.16,894.77 v 135.19 l -34.29,-26.48 -22.66,30.93 60.59,44.46 h 39.8 v -184.1 h -43.44\" /><path         id=\"path38\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1621.52,987.34 c 0,5.711 -0.35,12.039 -1.01,18.99 -0.71,6.91 -1.99,13.4 -3.91,19.37 -1.91,5.98 -4.65,11.02 -8.2,15.08 -3.56,4.06 -8.2,6.1 -13.91,6.1 -5.7,0 -10.39,-2.04 -14.02,-6.1 -3.67,-4.06 -6.49,-9.1 -8.48,-15.08 -1.99,-5.97 -3.32,-12.46 -4.02,-19.37 -0.7,-6.951 -1.06,-13.279 -1.06,-18.99 0,-5.891 0.36,-12.34 1.06,-19.371 0.7,-7.028 2.03,-13.52 4.02,-19.489 1.99,-5.98 4.81,-11.019 8.48,-15.082 3.63,-4.097 8.32,-6.128 14.02,-6.128 5.71,0 10.35,2.031 13.91,6.128 3.55,4.063 6.29,9.102 8.2,15.082 1.92,5.969 3.2,12.461 3.91,19.489 0.66,7.031 1.01,13.48 1.01,19.371 z m 44.73,0 c 0,-13 -1.29,-25.391 -3.91,-37.18 -2.57,-11.801 -6.75,-22.148 -12.46,-31.058 -5.74,-8.942 -13.12,-16.051 -22.22,-21.332 -9.11,-5.27 -20.16,-7.93 -33.17,-7.93 -13.01,0 -24.1,2.66 -33.28,7.93 -9.18,5.281 -16.68,12.39 -22.5,21.332 -5.82,8.91 -10,19.257 -12.62,31.058 -2.57,11.789 -3.86,24.18 -3.86,37.18 0,13.01 1.29,25.36 3.86,37.04 2.62,11.71 6.8,21.95 12.62,30.7 5.82,8.75 13.32,15.7 22.5,20.94 9.18,5.19 20.27,7.77 33.28,7.77 13.01,0 24.06,-2.58 33.17,-7.77 9.1,-5.24 16.48,-12.19 22.22,-20.94 5.71,-8.75 9.89,-18.99 12.46,-30.7 2.62,-11.68 3.91,-24.03 3.91,-37.04\" /><path         id=\"path40\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 972.031,605 v 135.199 l -34.332,-26.527 -22.621,30.937 60.582,44.493 h 39.81 V 605 h -43.439\" /><path         id=\"path42\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1125.08,605 v 135.199 l -34.34,-26.527 -22.62,30.937 60.59,44.493 h 39.81 V 605 h -43.44\" /><path         id=\"path44\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1277.46,605 v 135.199 l -34.34,-26.527 -22.57,30.937 60.54,44.493 h 39.81 V 605 h -43.44\" /><path         id=\"path46\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1463.71,697.582 c 0,5.699 -0.35,12.027 -1.05,18.938 -0.67,6.96 -2,13.402 -3.87,19.378 -1.91,5.981 -4.65,11.012 -8.2,15.082 -3.56,4.102 -8.21,6.129 -13.91,6.129 -5.74,0 -10.39,-2.027 -14.06,-6.129 -3.64,-4.07 -6.45,-9.101 -8.44,-15.082 -1.99,-5.976 -3.32,-12.418 -4.02,-19.378 -0.71,-6.911 -1.06,-13.239 -1.06,-18.938 0,-5.902 0.35,-12.352 1.06,-19.383 0.7,-7.027 2.03,-13.508 4.02,-19.488 1.99,-5.981 4.8,-11.012 8.44,-15.082 3.67,-4.098 8.32,-6.129 14.06,-6.129 5.7,0 10.35,2.031 13.91,6.129 3.55,4.07 6.29,9.101 8.2,15.082 1.87,5.98 3.2,12.461 3.87,19.488 0.7,7.031 1.05,13.481 1.05,19.383 z m 44.73,0 c 0,-13.012 -1.29,-25.391 -3.91,-37.191 -2.62,-11.801 -6.76,-22.153 -12.5,-31.09 -5.7,-8.91 -13.12,-16.02 -22.23,-21.289 -9.1,-5.313 -20.11,-7.93 -33.12,-7.93 -13.01,0 -24.1,2.617 -33.28,7.93 -9.18,5.269 -16.68,12.379 -22.5,21.289 -5.82,8.937 -10,19.289 -12.62,31.09 -2.58,11.8 -3.9,24.179 -3.9,37.191 0,12.969 1.32,25.348 3.9,37.027 2.62,11.723 6.8,21.911 12.62,30.661 5.82,8.789 13.32,15.75 22.5,20.98 9.18,5.16 20.27,7.77 33.28,7.77 13.01,0 24.02,-2.61 33.12,-7.77 9.11,-5.23 16.53,-12.191 22.23,-20.98 5.74,-8.75 9.88,-18.938 12.5,-30.661 2.62,-11.679 3.91,-24.058 3.91,-37.027\" /><path         id=\"path48\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1060,398.629 v 98.133 l -24.92,-19.223 -16.41,22.422 43.99,32.309 h 28.86 V 398.629 H 1060\" /><path         id=\"path50\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1280.98,398.629 v 98.133 l -24.93,-19.223 -16.44,22.422 43.98,32.309 h 28.91 V 398.629 h -31.52\" /><path         id=\"path52\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 971.68,465.82 c 0,4.141 -0.231,8.75 -0.739,13.789 -0.511,5 -1.453,9.692 -2.851,14.063 -1.371,4.34 -3.36,7.969 -5.942,10.937 -2.578,2.93 -5.937,4.411 -10.078,4.411 -4.179,0 -7.582,-1.481 -10.191,-4.411 -2.66,-2.968 -4.688,-6.597 -6.141,-10.937 -1.476,-4.371 -2.418,-9.063 -2.929,-14.063 -0.508,-5.039 -0.778,-9.648 -0.778,-13.789 0,-4.3 0.27,-8.98 0.778,-14.058 0.511,-5.082 1.453,-9.852 2.929,-14.184 1.453,-4.34 3.481,-7.969 6.141,-10.937 2.609,-2.969 6.012,-4.411 10.191,-4.411 4.141,0 7.5,1.442 10.078,4.411 2.582,2.968 4.571,6.597 5.942,10.937 1.398,4.332 2.34,9.102 2.851,14.184 0.508,5.078 0.739,9.758 0.739,14.058 z m 32.46,0 c 0,-9.449 -0.94,-18.441 -2.81,-26.992 -1.881,-8.558 -4.92,-16.098 -9.06,-22.539 -4.18,-6.519 -9.54,-11.68 -16.141,-15.508 -6.598,-3.832 -14.649,-5.742 -24.059,-5.742 -9.449,0 -17.5,1.91 -24.179,5.742 -6.68,3.828 -12.11,8.989 -16.332,15.508 -4.219,6.441 -7.258,13.981 -9.137,22.539 -1.91,8.551 -2.852,17.543 -2.852,26.992 0,9.41 0.942,18.399 2.852,26.879 1.879,8.512 4.918,15.93 9.137,22.301 4.222,6.328 9.652,11.41 16.332,15.199 6.679,3.75 14.73,5.66 24.179,5.66 9.41,0 17.461,-1.91 24.059,-5.66 6.601,-3.789 11.961,-8.871 16.141,-15.199 4.14,-6.371 7.179,-13.789 9.06,-22.301 1.87,-8.48 2.81,-17.469 2.81,-26.879\" /><path         id=\"path54\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1193.91,465.82 c 0,4.141 -0.24,8.75 -0.75,13.789 -0.5,5 -1.44,9.692 -2.85,14.063 -1.36,4.34 -3.36,7.969 -5.93,10.937 -2.58,2.93 -5.94,4.411 -10.08,4.411 -4.18,0 -7.58,-1.481 -10.2,-4.411 -2.65,-2.968 -4.72,-6.597 -6.13,-10.937 -1.49,-4.371 -2.46,-9.063 -2.93,-14.063 -0.51,-5.039 -0.78,-9.648 -0.78,-13.789 0,-4.3 0.27,-8.98 0.78,-14.058 0.47,-5.082 1.44,-9.852 2.93,-14.184 1.41,-4.34 3.48,-7.969 6.13,-10.937 2.62,-2.969 6.02,-4.411 10.2,-4.411 4.14,0 7.5,1.442 10.08,4.411 2.57,2.968 4.57,6.597 5.93,10.937 1.41,4.332 2.35,9.102 2.85,14.184 0.51,5.078 0.75,9.758 0.75,14.058 z m 32.46,0 c 0,-9.449 -0.94,-18.441 -2.82,-26.992 -1.91,-8.558 -4.92,-16.098 -9.06,-22.539 -4.18,-6.519 -9.53,-11.68 -16.13,-15.508 -6.6,-3.832 -14.65,-5.742 -24.06,-5.742 -9.46,0 -17.5,1.91 -24.18,5.742 -6.68,3.828 -12.11,8.989 -16.33,15.508 -4.22,6.441 -7.27,13.981 -9.14,22.539 -1.92,8.551 -2.85,17.543 -2.85,26.992 0,9.41 0.93,18.399 2.85,26.879 1.87,8.512 4.92,15.93 9.14,22.301 4.22,6.328 9.65,11.41 16.33,15.199 6.68,3.75 14.72,5.66 24.18,5.66 9.41,0 17.46,-1.91 24.06,-5.66 6.6,-3.789 11.95,-8.871 16.13,-15.199 4.14,-6.371 7.15,-13.789 9.06,-22.301 1.88,-8.48 2.82,-17.469 2.82,-26.879\" /><path         id=\"path56\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1648.83,398.629 v 98.133 l -24.92,-19.223 -16.45,22.422 43.99,32.309 h 28.9 V 398.629 h -31.52\" /><path         id=\"path58\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1561.76,465.82 c 0,4.141 -0.24,8.75 -0.74,13.789 -0.51,5 -1.45,9.692 -2.86,14.063 -1.36,4.34 -3.36,7.969 -5.93,10.937 -2.58,2.93 -5.94,4.411 -10.08,4.411 -4.18,0 -7.58,-1.481 -10.2,-4.411 -2.65,-2.968 -4.68,-6.597 -6.17,-10.937 -1.4,-4.371 -2.38,-9.063 -2.89,-14.063 -0.51,-5.039 -0.78,-9.648 -0.78,-13.789 0,-4.3 0.27,-8.98 0.78,-14.058 0.51,-5.082 1.49,-9.852 2.89,-14.184 1.49,-4.34 3.52,-7.969 6.17,-10.937 2.62,-2.969 6.02,-4.411 10.2,-4.411 4.14,0 7.5,1.442 10.08,4.411 2.57,2.968 4.57,6.597 5.93,10.937 1.41,4.332 2.35,9.102 2.86,14.184 0.5,5.078 0.74,9.758 0.74,14.058 z m 32.46,0 c 0,-9.449 -0.94,-18.441 -2.81,-26.992 -1.92,-8.558 -4.93,-16.098 -9.07,-22.539 -4.18,-6.519 -9.53,-11.68 -16.13,-15.508 -6.6,-3.832 -14.65,-5.742 -24.06,-5.742 -9.45,0 -17.5,1.91 -24.18,5.742 -6.68,3.828 -12.11,8.989 -16.33,15.508 -4.22,6.441 -7.26,13.981 -9.14,22.539 -1.91,8.551 -2.85,17.543 -2.85,26.992 0,9.41 0.94,18.399 2.85,26.879 1.88,8.512 4.92,15.93 9.14,22.301 4.22,6.328 9.65,11.41 16.33,15.199 6.68,3.75 14.73,5.66 24.18,5.66 9.41,0\
       17.46,-1.91 24.06,-5.66 6.6,-3.789 11.95,-8.871 16.13,-15.199 4.14,-6.371 7.15,-13.789 9.07,-22.301 1.87,-8.48 2.81,-17.469 2.81,-26.879\" /><path         id=\"path60\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1527.54,241.172 v 98.129 l -24.92,-19.262 -16.45,22.5 43.99,32.262 h 28.9 V 241.172 h -31.52\" /><path         id=\"path62\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1440.47,308.359 c 0,4.141 -0.24,8.75 -0.74,13.789 -0.51,5 -1.45,9.692 -2.85,14.063 -1.37,4.34 -3.36,7.969 -5.94,10.937 -2.58,2.93 -5.94,4.411 -10.08,4.411 -4.18,0 -7.58,-1.481 -10.2,-4.411 -2.65,-2.968 -4.68,-6.597 -6.13,-10.937 -1.44,-4.371 -2.42,-9.063 -2.93,-14.063 -0.51,-5.039 -0.78,-9.648 -0.78,-13.789 0,-4.3 0.27,-8.98 0.78,-14.058 0.51,-5.082 1.49,-9.852 2.93,-14.18 1.45,-4.34 3.48,-7.973 6.13,-10.941 2.62,-2.969 6.02,-4.41 10.2,-4.41 4.14,0 7.5,1.441 10.08,4.41 2.58,2.968 4.57,6.601 5.94,10.941 1.4,4.328 2.34,9.098 2.85,14.18 0.5,5.078 0.74,9.758 0.74,14.058 z m 32.46,0 c 0,-9.449 -0.94,-18.437 -2.81,-26.988 -1.88,-8.562 -4.92,-16.101 -9.07,-22.582 -4.14,-6.488 -9.53,-11.641 -16.13,-15.469 -6.6,-3.832 -14.65,-5.742 -24.06,-5.742 -9.45,0 -17.5,1.91 -24.18,5.742 -6.68,3.828 -12.11,8.981 -16.33,15.469 -4.22,6.481 -7.26,14.02 -9.14,22.582 -1.87,8.551 -2.85,17.539 -2.85,26.988 0,9.411 0.98,18.403 2.85,26.871 1.88,8.52 4.92,15.942 9.14,22.309 4.22,6.332 9.65,11.41 16.33,15.191 6.68,3.75 14.73,5.668 24.18,5.668 9.41,0 17.46,-1.918 24.06,-5.668 6.6,-3.781 11.99,-8.859 16.13,-15.191 4.15,-6.367 7.19,-13.789 9.07,-22.309 1.87,-8.468 2.81,-17.46 2.81,-26.871\" /><path         id=\"path64\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1015.9,243.09 v 68 l -17.271,-13.32 -11.359,15.589 30.46,22.34 h 20.04 V 243.09 h -21.87\" /><path         id=\"path66\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 955.59,289.648 c 0,2.891 -0.199,6.051 -0.512,9.571 -0.387,3.48 -1.019,6.722 -1.988,9.73 -0.942,3 -2.309,5.539 -4.11,7.571 -1.789,2.07 -4.14,3.089 -6.992,3.089 -2.886,0 -5.226,-1.019 -7.066,-3.089 -1.832,-2.032 -3.242,-4.571 -4.262,-7.571 -1.012,-3.008 -1.68,-6.25 -2.031,-9.73 -0.348,-3.52 -0.508,-6.68 -0.508,-9.571 0,-2.929 0.16,-6.207 0.508,-9.726 0.351,-3.551 1.019,-6.801 2.031,-9.801 1.02,-3.012 2.43,-5.551 4.262,-7.582 1.84,-2.07 4.18,-3.09 7.066,-3.09 2.852,0 5.203,1.02 6.992,3.09 1.801,2.031 3.168,4.57 4.11,7.582 0.969,3 1.601,6.25 1.988,9.801 0.313,3.519 0.512,6.797 0.512,9.726 z m 22.5,0 c 0,-6.527 -0.668,-12.769 -1.961,-18.707 -1.328,-5.902 -3.399,-11.14 -6.289,-15.632 -2.891,-4.489 -6.602,-8.039 -11.211,-10.7 -4.57,-2.66 -10.109,-4.019 -16.641,-4.019 -6.558,0 -12.148,1.359 -16.758,4.019 -4.609,2.661 -8.39,6.211 -11.32,10.7 -2.93,4.492 -5.039,9.73 -6.332,15.632 -1.328,5.938 -1.957,12.18 -1.957,18.707 0,6.563 0.629,12.774 1.957,18.633 1.293,5.899 3.402,11.059 6.332,15.469 2.93,4.371 6.711,7.93 11.32,10.512 4.61,2.617 10.2,3.937 16.758,3.937 6.532,0 12.071,-1.32 16.641,-3.937 4.609,-2.582 8.32,-6.141 11.211,-10.512 2.89,-4.41 4.961,-9.57 6.289,-15.469 1.293,-5.859 1.961,-12.07 1.961,-18.633\" /><path         id=\"path68\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1287.77,124.141 v 68.007 l -17.26,-13.32 -11.37,15.551 30.47,22.383 h 20 v -92.621 h -21.84\" /><path         id=\"path70\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1227.46,170.699 c 0,2.891 -0.19,6.063 -0.55,9.571 -0.35,3.48 -0.97,6.718 -1.95,9.73 -0.98,3.012 -2.34,5.551 -4.1,7.578 -1.8,2.07 -4.14,3.082 -7.03,3.082 -2.85,0 -5.24,-1.012 -7.03,-3.082 -1.84,-2.027 -3.28,-4.566 -4.26,-7.578 -1.02,-3.012 -1.68,-6.25 -2.03,-9.73 -0.35,-3.508 -0.55,-6.68 -0.55,-9.571 0,-2.969 0.2,-6.211 0.55,-9.719 0.35,-3.558 1.01,-6.8 2.03,-9.851 0.98,-3.008 2.42,-5.508 4.26,-7.578 1.79,-2.031 4.18,-3.039 7.03,-3.039 2.89,0 5.23,1.008 7.03,3.039 1.76,2.07 3.12,4.57 4.1,7.578 0.98,3.051 1.6,6.293 1.95,9.851 0.36,3.508 0.55,6.75 0.55,9.719 z m 22.5,0 c 0,-6.519 -0.66,-12.769 -1.99,-18.711 -1.29,-5.937 -3.4,-11.129 -6.25,-15.617 -2.89,-4.492 -6.6,-8.09 -11.21,-10.75 -4.57,-2.652 -10.12,-3.941 -16.68,-3.941 -6.53,0 -12.11,1.289 -16.72,3.941 -4.65,2.66 -8.4,6.258 -11.33,10.75 -2.93,4.488 -5.04,9.68 -6.33,15.617 -1.33,5.942 -1.99,12.192 -1.99,18.711 0,6.531 0.66,12.781 1.99,18.641 1.29,5.89 3.4,11.051 6.33,15.43 2.93,4.41 6.68,7.929 11.33,10.539 4.61,2.621 10.19,3.91 16.72,3.91 6.56,0 12.11,-1.289 16.68,-3.91 4.61,-2.61 8.32,-6.129 11.21,-10.539 2.85,-4.379 4.96,-9.54 6.25,-15.43 1.33,-5.86 1.99,-12.11 1.99,-18.641\" /><path         id=\"path72\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1661.02,308.359 c 0,4.141 -0.24,8.75 -0.75,13.789 -0.5,5 -1.44,9.692 -2.85,14.063 -1.37,4.34 -3.36,7.969 -5.94,10.937 -2.57,2.93 -5.93,4.411 -10.07,4.411 -4.14,0 -7.58,-1.481 -10.2,-4.411 -2.66,-2.968 -4.69,-6.597 -6.13,-10.937 -1.45,-4.371 -2.42,-9.063 -2.93,-14.063 -0.51,-5.039 -0.74,-9.648 -0.74,-13.789 0,-4.3 0.23,-8.98 0.74,-14.058 0.51,-5.082 1.48,-9.852 2.93,-14.18 1.44,-4.34 3.47,-7.973 6.13,-10.941 2.62,-2.969 6.06,-4.41 10.2,-4.41 4.14,0 7.5,1.441 10.07,4.41 2.58,2.968 4.57,6.601 5.94,10.941 1.41,4.328 2.35,9.098 2.85,14.18 0.51,5.078 0.75,9.758 0.75,14.058 z m 32.5,0 c 0,-9.449 -0.98,-18.437 -2.86,-26.988 -1.87,-8.562 -4.92,-16.101 -9.06,-22.582 -4.14,-6.488 -9.53,-11.641 -16.13,-15.469 -6.6,-3.832 -14.61,-5.742 -24.06,-5.742 -9.46,0 -17.5,1.91 -24.18,5.742 -6.64,3.828 -12.11,8.981 -16.33,15.469 -4.22,6.481 -7.27,14.02 -9.14,22.582 -1.88,8.551 -2.85,17.539 -2.85,26.988 0,9.411 0.97,18.403 2.85,26.871 1.87,8.52 4.92,15.942 9.14,22.309 4.22,6.332 9.69,11.41 16.33,15.191 6.68,3.75 14.72,5.668 24.18,5.668 9.45,0 17.46,-1.918 24.06,-5.668 6.6,-3.781 11.99,-8.859 16.13,-15.191 4.14,-6.367 7.19,-13.789 9.06,-22.309 1.88,-8.468 2.86,-17.46 2.86,-26.871\" /><path         id=\"path74\"         style=\"fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none\"         d=\"m 1600.16,1210.51 c -30.82,150.58 -164.93,259.88 -318.87,259.88 -23.44,0 -46.49,-2.66 -68.95,-7.5 -37.42,219.49 -228.86,387.15 -458.86,387.15 -227.859,0 -417.859,-164.57 -457.742,-381.06 C 130.16,1453.91 0,1314.38 0,1144.92 0,965.469 146.02,819.488 325.469,819.488 h 486.953 c 24.848,0 45,20.121 45,45 0,24.852 -20.152,45 -45,45 H 325.469 C 195.621,909.488 90,1015.12 90,1144.92 c 0,129.85 105.621,235.47 235.469,235.47 47.191,0 92.691,-13.87 131.601,-40.16 20.629,-13.9 48.59,-8.51 62.5,12.07 13.91,20.59 8.481,48.6 -12.109,62.5 -36.762,24.85 -77.813,41.45 -120.902,49.65 36.761,168.79 187.269,295.59 366.921,295.59 191.399,0 349.68,-143.91 372.61,-329.18 -12.07,-6.56 -23.86,-13.75 -35.15,-21.91 -20.16,-14.54 -24.69,-42.66 -10.16,-62.82 14.57,-20.15 42.7,-24.68 62.85,-10.15 40.24,29.06 87.85,44.41 137.66,44.41 111.41,0 208.4,-79.02 230.66,-187.97 4.38,-21.29 23.13,-35.97 44.07,-35.97 2.96,0 6.01,0.31 9.06,0.93 24.33,4.96 40.04,28.75 35.08,53.13\" /></g></g></svg>    </svg>"
print(svg)