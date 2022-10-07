import { writable } from 'svelte/store';

export const crop_xy_store = writable<number>();
export const crop_size_store = writable<number>();