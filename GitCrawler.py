import os
import sys

file = open("ROI_Organizations.md")

start_point_exist = 0
start_point_found = 0

if len(sys.argv) > 1 :
	start_point_exist = 1

for line in file.readlines():
    line = line.strip('\n')
    line_elements = line.split(' ')
    if len(line_elements) >= 2:
        print(line_elements[1])

        if(start_point_exist) :
            if (line_elements[1] == sys.argv[1]) :
                start_point_found = 1

            if (start_point_found) :
                exi = os.path.exists(line_elements[1])
                if line_elements[2] == 'o':
                    # 如果目录不存在
                    if not exi:
                        # 创建目录
                        os.mkdir(line_elements[1])
                        # 进入目录
                        os.chdir(line_elements[1])

                        # 执行脚本拉取操作
                        cmd_string = "ghcloneall --include-forks --init --org "+line_elements[1]+" --verbose && ghcloneall --verbose"
                        # print(cmd_string)
                        os.system(cmd_string)

                        # 离开目录
                        os.chdir("..")
                    # 如果目录存在
                    else:
                        # 进入目录
                        os.chdir(line_elements[1])

                        # 遍历所有子目录
                        dirs = os.listdir("./")
                        for sub_dir in dirs:
                            if not sub_dir[0] == '.':
                                print(sub_dir)
                                os.chdir(sub_dir)
                                os.system("git pull")
                                os.chdir("..")
                            pass

                        # 执行脚本拉取操作
                        cmd_string = "ghcloneall --include-forks --init --org "+line_elements[1]+" --verbose && ghcloneall --verbose"
                        os.system(cmd_string)

                        # 离开目录
                        os.chdir("..")
                        pass
                else:
                    # 如果目录不存在
                    if not exi:
                        # 创建目录
                        os.mkdir(line_elements[1])
                        # 进入目录
                        os.chdir(line_elements[1])

                        # 执行脚本拉取操作
                        cmd_string = "ghcloneall --include-forks --init --user "+line_elements[1]+" --verbose && ghcloneall --verbose"
                        # print(cmd_string)
                        os.system(cmd_string)

                        # 离开目录
                        os.chdir("..")
                    # 如果目录存在
                    else:
                        # 进入目录
                        os.chdir(line_elements[1])

                        # 遍历所有子目录
                        dirs = os.listdir("./")
                        for sub_dir in dirs:
                            if not sub_dir[0] == '.':
                                print(sub_dir)
                                os.chdir(sub_dir)
                                os.system("git pull")
                                os.chdir("..")
                            pass

                        # 执行脚本拉取操作
                        cmd_string = "ghcloneall --include-forks --init --user "+line_elements[1]+" --verbose && ghcloneall --verbose"
                        # print(cmd_string)
                        os.system(cmd_string)

                        # 离开目录
                        os.chdir("..")
                        pass

        else:
            exi = os.path.exists(line_elements[1])
            if line_elements[2] == 'o':
                # 如果目录不存在
                if not exi:
                    # 创建目录
                    os.mkdir(line_elements[1])
                    # 进入目录
                    os.chdir(line_elements[1])

                    # 执行脚本拉取操作
                    cmd_string = "ghcloneall --include-forks --init --org " + line_elements[
                        1] + " --verbose && ghcloneall --verbose"
                    # print(cmd_string)
                    os.system(cmd_string)

                    # 离开目录
                    os.chdir("..")
                # 如果目录存在
                else:
                    # 进入目录
                    os.chdir(line_elements[1])

                    # 遍历所有子目录
                    dirs = os.listdir("./")
                    for sub_dir in dirs:
                        if not sub_dir[0] == '.':
                            print(sub_dir)
                            os.chdir(sub_dir)
                            os.system("git pull")
                            os.chdir("..")
                        pass

                    # 执行脚本拉取操作
                    cmd_string = "ghcloneall --include-forks --init --org " + line_elements[
                        1] + " --verbose && ghcloneall --verbose"
                    os.system(cmd_string)

                    # 离开目录
                    os.chdir("..")
                    pass
            else:
                # 如果目录不存在
                if not exi:
                    # 创建目录
                    os.mkdir(line_elements[1])
                    # 进入目录
                    os.chdir(line_elements[1])

                    # 执行脚本拉取操作
                    cmd_string = "ghcloneall --include-forks --init --user " + line_elements[
                        1] + " --verbose && ghcloneall --verbose"
                    # print(cmd_string)
                    os.system(cmd_string)

                    # 离开目录
                    os.chdir("..")
                # 如果目录存在
                else:
                    # 进入目录
                    os.chdir(line_elements[1])

                    # 遍历所有子目录
                    dirs = os.listdir("./")
                    for sub_dir in dirs:
                        if not sub_dir[0] == '.':
                            print(sub_dir)
                            os.chdir(sub_dir)
                            os.system("git pull")
                            os.chdir("..")
                        pass

                    # 执行脚本拉取操作
                    cmd_string = "ghcloneall --include-forks --init --user " + line_elements[
                        1] + " --verbose && ghcloneall --verbose"
                    # print(cmd_string)
                    os.system(cmd_string)

                    # 离开目录
                    os.chdir("..")
                    pass

