from pathlib import Path
import ffmpeg

test_file = Path.home() / "Downloads" / "test.mp4"


class PostProcessor:
    def __init__(self) -> None:
        self.source_duration = None

    def get_source_duration(self, input_file):
        get_info = ffmpeg.probe(input_file)
        self.source_duration = round(float(get_info["format"]["duration"]), 2)
        # return self.source_duration

    def compress(self, input_file, tar_file_size):
        get_file = Path(input_file)
        get_file_parent = Path(input_file).parent
        get_file_name = Path(input_file).stem
        get_file_ext = Path(input_file).suffix

        # require source duration first
        audio_br = 128
        tar_file_size = float(tar_file_size)
        video_br = int(((tar_file_size * 8192) / self.source_duration) - audio_br)

        output_file = get_file_parent / f"{get_file_name}_comp{get_file_ext}"

        options = ffmpeg.input(get_file).output(
            str(output_file), video_bitrate=f"{video_br}k", audio_bitrate=f"{audio_br}k"
        )

        ffmpeg.run(options)

    def timeline_cut(self, input_file, start_sec, end_sec):
        get_file = Path(input_file)
        get_file_parent = Path(input_file).parent
        get_file_name = Path(input_file).stem
        get_file_ext = Path(input_file).suffix

        output_file = get_file_parent / f"{get_file_name}_cut{get_file_ext}"

        options = ffmpeg.input(get_file, ss=start_sec, to=end_sec).output(
            str(output_file)
        )

        ffmpeg.run(options)

    def convert(self, input_file, output_format):
        get_file = Path(input_file)
        get_file_parent = Path(input_file).parent
        get_file_name = Path(input_file).stem

        output_file = get_file_parent / f"{get_file_name}_conv.{output_format}"

        options = ffmpeg.input(get_file).output(str(output_file))

        ffmpeg.run(options)


pp = PostProcessor()

# print(pp.get_source_duration(test_file))
# pp.timeline_cut(test_file, "1.0", "3.0")
# pp.compress(test_file, "2")
# pp.convert(test_file, "webm")
