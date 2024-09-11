# Copyright ⓒ 2024 김대영 all rights reserved
# 이 코드는 배포 및 판매가 불가합니다.

import tkinter as tk
import tkinter.messagebox 
import subprocess
import os

root = tk.Tk()
user_name = os.getlogin()

root.title('컴퓨터 최적화 프로그램 ver.1.0')
root.geometry('600x500+100+100')

# 상태 메시지 레이블 추가
status_label = tk.Label(root, text="상태: 준비 완료", width=50, height=2, font=('맑은 고딕', 12))
status_label.grid(row=3, column=0, columnspan=3, pady=10)

label1 = tk.Label(root, 
                  text="최적화 프로그램",
                  width=30,
                  height=4,
                  font=('맑은 고딕', 14, 'bold'))
label1.grid(row=0, column=0, columnspan=3, pady=20)

# 상태 업데이트 함수
def update_status(message):
    status_label.config(text=f"상태: {message}")
    root.update()

# 함수
def run_disk():
    update_status("임시파일 삭제 중...")
    subprocess.run('rmdir /s /q C:\Windows\Temp', shell=True)
    subprocess.run(f'rmdir /s /q C:\\Users\\{user_name}\\AppData\\Local\\Temp', shell=True)

    # 다운로드 폴더 내의 파일들 삭제
    downloads_folder = f'C:\\Users\\{user_name}\\Downloads'
    if os.path.exists(downloads_folder):
        delete_files_confirm = tkinter.messagebox.askyesno("다운로드 폴더 파일 삭제", "다운로드 폴더의 모든 파일들을 삭제하시겠습니까?")
        if delete_files_confirm:
            for filename in os.listdir(downloads_folder):
                file_path = os.path.join(downloads_folder, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            update_status("다운로드 폴더 파일 삭제 완료")
        else:
            update_status("다운로드 폴더 파일 삭제가 취소되었습니다.")
    else:
        update_status("다운로드 폴더가 존재하지 않습니다.")

    cipher_confirm = tkinter.messagebox.askyesno("디스크 공간 확보", "파일 삭제 데이터를 복구할 수 없게 됩니다. 계속하시겠습니까?")
    if cipher_confirm:
        subprocess.run('cipher /w:c:', shell=True)
        update_status("디스크 정리 완료")
    else:
        update_status("디스크 정리가 취소되었습니다.")
    
    subprocess.run('wsreset.exe', shell=True)
    update_status("OS 압축 중...")
    subprocess.run('compact.exe /compactOS:always', shell=True)

    # cipher /w:c 명령에 대한 사용자 확인

def run_speed_up():
    update_status("속도 향상 중...")
    subprocess.run('powercfg -h off', shell=True)
    update_status("네트워크 최적화 중...")
    subprocess.run('netsh interface tcp set global autotuninglevel=highlyrestricted', shell=True)
    subprocess.run('ipconfig /flushdns', shell=True)
    update_status("속도 향상 완료")

def run_system_check():
    update_status("시스템 점검 중...")
    subprocess.run('sfc /scannow', shell=True)
    update_status("시스템 점검 완료")

def run_all():
    update_status("시스템 점검 중...")
    subprocess.run('sfc /scannow', shell=True)
    update_status("시스템 점검 완료")
    update_status("속도 향상 중...")
    subprocess.run('powercfg -h off', shell=True)
    update_status("네트워크 최적화 중...")
    subprocess.run('netsh interface tcp set global autotuninglevel=highlyrestricted', shell=True)
    subprocess.run('ipconfig /flushdns', shell=True)
    update_status("속도 향상 완료")
    update_status("임시파일 삭제 중...")
    subprocess.run('rmdir /s /q C:\Windows\Temp', shell=True)
    subprocess.run(f'rmdir /s /q C:\\Users\\{user_name}\\AppData\\Local\\Temp', shell=True)

    # 다운로드 폴더 내의 파일들 삭제
    downloads_folder = f'C:\\Users\\{user_name}\\Downloads'
    if os.path.exists(downloads_folder):
        delete_files_confirm = tkinter.messagebox.askyesno("다운로드 폴더 파일 삭제", "다운로드 폴더의 모든 파일들을 삭제하시겠습니까?")
        if delete_files_confirm:
            for filename in os.listdir(downloads_folder):
                file_path = os.path.join(downloads_folder, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            update_status("다운로드 폴더 파일 삭제 완료")
        else:
            update_status("다운로드 폴더 파일 삭제가 취소되었습니다.")
    else:
        update_status("다운로드 폴더가 존재하지 않습니다.")

    cipher_confirm = tkinter.messagebox.askyesno("디스크 공간 확보", "파일 삭제 데이터를 복구할 수 없게 됩니다. 계속하시겠습니까?")
    if cipher_confirm:
        subprocess.run('cipher /w:c:', shell=True)
        update_status("디스크 정리 완료")
    else:
        update_status("디스크 정리가 취소되었습니다.")
    
    subprocess.run('wsreset.exe', shell=True)
    update_status("OS 압축 중...")
    subprocess.run('compact.exe /compactOS:always', shell=True)

    # 다운로드 폴더 내의 파일들 삭제
    downloads_folder = f'C:\\Users\\{user_name}\\Downloads'
    if os.path.exists(downloads_folder):
        delete_files_confirm = tkinter.messagebox.askyesno("다운로드 폴더 파일 삭제", "다운로드 폴더의 모든 파일들을 삭제하시겠습니까?")
        if delete_files_confirm:
            for filename in os.listdir(downloads_folder):
                file_path = os.path.join(downloads_folder, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            update_status("다운로드 폴더 파일 삭제 완료")
        else:
            update_status("다운로드 폴더 파일 삭제가 취소되었습니다.")
    else:
        update_status("다운로드 폴더가 존재하지 않습니다.")

    cipher_confirm = tkinter.messagebox.askyesno("디스크 공간 확보", "파일 삭제 데이터를 복구할 수 없게 됩니다. 계속하시겠습니까?")
    if cipher_confirm:
        subprocess.run('cipher /w:c:', shell=True)
        update_status("디스크 정리 완료")
    else:
        update_status("디스크 정리가 취소되었습니다.")
    
    subprocess.run('wsreset.exe', shell=True)
    update_status("OS 압축 중...")
    subprocess.run('compact.exe /compactOS:always', shell=True)
    update_status("완료")
    

#################################################################################################################################

button1 = tk.Button(root, text='디스크 정리', font=('맑은 고딕', 12, 'bold'), bg='blue', fg='white', width=17, height=2, command=run_disk)
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = tk.Button(root, text='속도 향상', font=('맑은 고딕', 12, 'bold'), bg='blue', fg='white', width=17, height=2,command=run_speed_up)
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = tk.Button(root, text='시스템 점검', font=('맑은 고딕', 12, 'bold'), bg='blue', fg='white', width=17, height=2, command=run_system_check)
button3.grid(row=1, column=2, padx=10, pady=10)

button4 = tk.Button(root, text='전체 최적화', font=('맑은 고딕', 14, 'bold'), bg='black', fg='white', width=49, height=3, command=run_all)
button4.grid(row=2, column=0, columnspan=3, pady=20)

#################################################################################################################################

info_label1 = tk.Label(root, 
                       text="실행중 '응답없음' 은 정상입니다. Copyright ⓒ 2024 김대영 all rights reserved", 
                       width=70, 
                       height=2, 
                       font=('맑은 고딕', 10))
info_label1.grid(row=4, column=0, columnspan=3, pady=5)

root.mainloop()
