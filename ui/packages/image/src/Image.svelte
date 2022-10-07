<script lang="ts">
	import { createEventDispatcher } from "svelte";
	import { BlockLabel } from "@gradio/atoms";
	import { Image, Sketch as SketchIcon } from "@gradio/icons";

	import Cropper from "./Cropper.svelte";
	import Sketch from "./Sketch.svelte";
	import Webcam from "./Webcam.svelte";
	import ModifySketch from "./ModifySketch.svelte";
	import BoostxTest from "../../app/src/components/Textbox/boostx_test1_no_used.svelte"

	import { Upload, ModifyUpload } from "@gradio/upload";

	export let value: null | string;
	export let label: string | undefined = undefined;
	export let show_label: boolean;

	export let source: "canvas" | "webcam" | "upload" = "upload";
	export let tool: "editor" | "select" = "editor";

	export let drop_text: string = "Drop an image file";
	export let or_text: string = "or";
	export let upload_text: string = "click to upload";
	export let streaming: boolean = false;
	export let pending: boolean = false;

	import { canvas_image_xywh_store } from '../../../../ui/packages/app/src/components/Textbo1/stores';
	import { crop_image_xywh_store } from '../../../../ui/packages/app/src/components/Textbo2/stores';


	let value_xy: '123' | string;
	let sketch: Sketch;

	function handle_upload({ detail }: CustomEvent<string>) {
		console.log("handle_upload...")
		console.log({detail})
		value = detail;
	}

	function handle_clear({ detail }: CustomEvent<null>) {
		value = null;
		dispatch("clear");
	}

	function handle_save({ detail }: { detail: string }) {
		value = detail.image_tmp;
		canvas_image_xywh_store.update(n => detail.canvas_image_xywh_tmp);
		crop_image_xywh_store.update(n => detail.crop_image_xywh_tmp);
		console.log("handle_save...")
		console.log({detail})
		// alert("boostx: handle_save canvas_image_xywh:"+detail.image_tmp + " crop_image_xywh: "+detail.crop_image_xywh_tmp);
		dispatch(streaming ? "stream" : "edit");
	}

	const dispatch = createEventDispatcher<{
		change: string | null;
		stream: string | null;
		edit: undefined;
		clear: undefined;
		drag: boolean;
	}>();

	$: dispatch("change", value);

	let dragging = false;

	$: dispatch("drag", dragging);
</script>

<BlockLabel
	{show_label}
	Icon={source === "canvas" ? SketchIcon : Image}
	label={label || (source === "canvas" ? "Sketch" : "Image")}
/>

<div class:bg-gray-200={value} class:h-60={source !== "webcam"}>
	{#if source === "canvas"}
		<ModifySketch
			on:undo={() => sketch.undo()}
			on:clear={() => sketch.clear()}
		/>
		<Sketch {value} bind:this={sketch} on:change={handle_save} />
	{:else if value === null || streaming}
		{#if source === "upload"}
			<Upload
				bind:dragging
				filetype="image/x-png,image/gif,image/jpeg"
				on:load={handle_upload}
				include_file_metadata={false}
			>
				<div class="flex flex-col">
					{drop_text}
					<span class="text-gray-300">- {or_text} -</span>
					{upload_text}
				</div>
			</Upload>
		{:else if source === "webcam"}
			<Webcam
				on:capture={handle_save}
				on:stream={handle_save}
				{streaming}
				{pending}
			/>
		{/if}
	{:else if tool === "select"}
		<Cropper image={value} on:crop={handle_save} />
		<ModifyUpload on:clear={(e) => (handle_clear(e), (tool = "editor"))} />
	{:else if tool === "editor"}
		<ModifyUpload
			on:edit={() => (tool = "select")}
			on:clear={handle_clear}
			editable
		/>

		<img class="w-full h-full object-contain" src={value} alt="" />
	{:else}
		<img class="w-full h-full object-contain" src={value} alt="" />
	{/if}
</div>
