import os
import json
import argparse
import csv
import torch
import base64
import numpy as np
from PIL import Image
from io import BytesIO


if __name__ == '__main__':
    ######################################################
    # TRAIN DATA
    ######################################################
    
    SPLIT = ['train', 'val']
    for split in SPLIT:
        IMAGE_ROOT = './data/images/{}'.format(split)
        f = open("./data/prograsp_{}.json".format(split), "r")
        data = json.load(f)
        f.close()
        
        # preprocess data for questioner
        print('data for questioner doing...')
        q_tsv_path = './data/{}_questioner.tsv'.format(split)
        with open(q_tsv_path, 'w', newline='') as f:
            tsv_out = csv.writer(f, delimiter='\t')
            for idx, sample in enumerate(data):
                # index
                item = []
                item.append(idx)

                # dialog context
                item.append(sample['instruction'])            

                # bounding box
                item.append(
                    "{},{},{},{}".format(
                        sample['bbox_cands'][0][0], 
                        sample['bbox_cands'][0][1],
                        sample['bbox_cands'][0][2],
                        sample['bbox_cands'][0][3]
                    )
                )

                # target sentence
                item.append(sample['question1'])

                # image
                img = Image.open(os.path.join(IMAGE_ROOT, sample['image_name']))
                img_buffer = BytesIO()
                img.save(img_buffer, format=img.format)
                byte_data = img_buffer.getvalue()
                base64_str = base64.b64encode(byte_data)
                base64_str = base64_str.decode("utf-8")
                item.append(base64_str)
                tsv_out.writerow(item)
               
        # preprocess data for answerer
        print('data for answerer doing...')
        a_tsv_path = './data/{}_answerer.tsv'.format(split)
        with open(a_tsv_path, 'w', newline='') as f:
            tsv_out = csv.writer(f, delimiter='\t')
            for idx, sample in enumerate(data):
                # index
                item = []
                item.append(idx)

                # question
                item.append(sample['question1'])

                # bounding box
                item.append(
                    "{},{},{},{}".format(
                        sample['bbox_cands'][sample['gt_bbox']][0],
                        sample['bbox_cands'][sample['gt_bbox']][1],
                        sample['bbox_cands'][sample['gt_bbox']][2],
                        sample['bbox_cands'][sample['gt_bbox']][3]
                    )
                )

                # answer
                item.append(sample['answer1'])

                # image
                img = Image.open(os.path.join(IMAGE_ROOT, sample['image_name']))
                img_buffer = BytesIO()
                img.save(img_buffer, format=img.format)
                byte_data = img_buffer.getvalue()
                base64_str = base64.b64encode(byte_data)
                base64_str = base64_str.decode("utf-8")
                item.append(base64_str)
                tsv_out.writerow(item)
        
        # preprocess data for visual grounding
        print('data for visual grounding doing...')
        v_tsv_path = './data/{}_vg.tsv'.format(split)
        with open(v_tsv_path, 'w', newline='') as f:
            tsv_out = csv.writer(f, delimiter='\t')
            for idx, sample in enumerate(data):
                ################ 
                # ROUND 1
                ################
                # index
                item1 = []
                item1.append(idx)

                # dummy
                item1.append(idx)

                # bounding box
                bbox_cands = np.array(sample['bbox_cands']) 
                tlxs = [bbox[0] for bbox in bbox_cands]
                tlxs = np.array(tlxs)
                indices = np.argsort(tlxs)

                flattened_bbox = [str(item) for sublist in bbox_cands[indices] for item in sublist]
                flattened_bbox = ",".join(flattened_bbox)
                item1.append(flattened_bbox)

                # dialog context
                item1.append(sample['instruction'])

                # image
                img = Image.open(os.path.join(IMAGE_ROOT, sample['image_name']))
                img_buffer = BytesIO()
                img.save(img_buffer, format=img.format)
                byte_data = img_buffer.getvalue()
                base64_str = base64.b64encode(byte_data)
                base64_str = base64_str.decode("utf-8")
                item1.append(base64_str)
                tsv_out.writerow(item1)
            
                ###############
                # ROUND 2
                ##############
                # index
                item2 = []
                item2.append(idx)

                # dummy
                item2.append(idx)

                # bounding box
                item2.append(
                    "{},{},{},{}".format(
                        sample['bbox_cands'][sample['gt_bbox']][0],
                        sample['bbox_cands'][sample['gt_bbox']][1],
                        sample['bbox_cands'][sample['gt_bbox']][2],
                        sample['bbox_cands'][sample['gt_bbox']][3]
                    )
                )

                # dialog context
                dc = []
                dc.append(sample['instruction'])
                dc.append(sample['question1'])
                dc.append(sample['answer1'])
                dc = "/".join(dc)
                item2.append(dc)

                # image
                img = Image.open(os.path.join(IMAGE_ROOT, sample['image_name']))
                img_buffer = BytesIO()
                img.save(img_buffer, format=img.format)
                byte_data = img_buffer.getvalue()
                base64_str = base64.b64encode(byte_data)
                base64_str = base64_str.decode("utf-8")
                item2.append(base64_str)
                tsv_out.writerow(item2)

    ######################################################
    # VALIDATION DATA
    ######################################################
    SPLIT = ['val']
    for split in SPLIT:
        IMAGE_ROOT = './data/images/{}'.format(split)
        f = open("./data/prograsp_{}.json".format(split), "r")
        data = json.load(f)
        f.close()

        # preprocess data for questioner
        print('data for {} doing...'.format(split))
        v_tsv_path = './data/{}_common.tsv'.format(split)
        with open(v_tsv_path, 'w', newline='') as f:
            tsv_out = csv.writer(f, delimiter='\t')
            for idx, sample in enumerate(data):
                # index
                item1 = []
                item1.append(idx)

                # dummy
                item1.append(idx)

                # bounding box
                item1.append(
                    "{},{},{},{}".format(
                        sample['bbox_cands'][sample['gt_bbox']][0],
                        sample['bbox_cands'][sample['gt_bbox']][1],
                        sample['bbox_cands'][sample['gt_bbox']][2],
                        sample['bbox_cands'][sample['gt_bbox']][3]
                    )
                )

                # dialog context
                dc = []
                dc.append(sample['instruction'])
                dc.append(sample['question1'])
                dc.append(sample['answer1'])
                dc = "/".join(dc)
                item1.append(dc)

                # image
                img = Image.open(os.path.join(IMAGE_ROOT, sample['image_name']))
                img_buffer = BytesIO()
                img.save(img_buffer, format=img.format)
                byte_data = img_buffer.getvalue()
                base64_str = base64.b64encode(byte_data)
                base64_str = base64_str.decode("utf-8")
                item1.append(base64_str)
                tsv_out.writerow(item1)

    
    ##############################################################
    # TEST-{SEEN, UNSEEN, SEEN_CLUTTERED} DATA
    ##############################################################
    SPLIT = ['test_seen_cluttered']
    for split in SPLIT:
        IMAGE_ROOT = './data/images/{}/'.format(split)
        f = open("./data/prograsp_{}.json".format(split), "r")
        data = json.load(f)
        f.close()

        # preprocess data for visual grounding
        print('data for {} doing...'.format(split))
        v_tsv_path = './data/{}_common.tsv'.format(split)
        with open(v_tsv_path, 'w', newline='') as f:
            tsv_out = csv.writer(f, delimiter='\t')
            for idx, sample in enumerate(data):
                # index
                item1 = []
                item1.append(idx)

                # dummy
                item1.append(idx)

                # bounding box
                flattened_bbox = [str(item) for sublist in sample['bbox_cands'] for item in sublist]
                flattened_bbox = ",".join(flattened_bbox) 
                item1.append(flattened_bbox)

                # dialog context
                item1.append(sample['instruction'])

                # image
                img = Image.open(os.path.join(IMAGE_ROOT, sample['image_name']))
                img_buffer = BytesIO()
                img.save(img_buffer, format=img.format)
                byte_data = img_buffer.getvalue()
                base64_str = base64.b64encode(byte_data)
                base64_str = base64_str.decode("utf-8")
                item1.append(base64_str)
                tsv_out.writerow(item1)
