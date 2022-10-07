<svelte:options accessors={true} />

<script lang="ts">
	import { TextBox } from "@gradio/form";
	import { Block } from "@gradio/atoms";
	import StatusTracker from "../StatusTracker/StatusTracker.svelte";
	import type { LoadingStatus } from "../StatusTracker/types";

	export let label: string = "Textbox";
	export let elem_id: string = "";
	export let value: string = "";
	export let lines: number;
	export let placeholder: string = "";
	export let form_position: "first" | "last" | "mid" | "single" = "single";
	export let show_label: boolean;
	export let max_lines: number | false;

	export let style: Record<string, unknown> = {};

	export let loading_status: LoadingStatus;

	export let mode: "static" | "dynamic";

	import { canvas_image_xywh_store } from './stores.ts';
	// export let crop_xy_val; 
	// crop_xy_store.set(0);
	canvas_image_xywh_store.subscribe(val => {
		value = val;
	});
</script>
<Block
	{form_position}
	{elem_id}
	disable={typeof style.container === "boolean" && !style.container}
>
	<StatusTracker {...loading_status} />

		<!-- bind:value={$crop_xy_store} -->
	<TextBox
		{style}
		bind:value
		{label}
		{show_label}
		{lines}
		max_lines={!max_lines && mode === "static" ? lines + 1 : max_lines}
		{placeholder}
		on:change
		on:submit
		disabled={mode === "static"}
	/>
	<!-- <input bind:value={$crop_xy_store}>
	<h1>The crop_xy_store is {$crop_xy_store}</h1>
	<h1>The crop_xy_store is {crop_xy_val}</h1> -->
</Block>
